import streamlit as st
import requests

def available():
    st.markdown(":color[**Available!**]{foreground = 'green'}", text_alignment = "right", width = "stretch")
    
def unavailable():
    st.markdown(":color[**Not Available!**]{foreground = 'red'}", text_alignment = "right", width = "stretch")

def error():
    st.markdown(":color[**ERROR!!**]{foreground = 'darkred'}", text_alignment = "right", width = "stretch")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
    )
}

def _check_instagram(name):
    headers = {**HEADERS, "X-IG-App-ID": "936619743392459", "Accept": "*/*"}
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={name}"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        return True
    if r.status_code == 404:
        return False
    return None  # rate-limited / blocked / unexpected response

def _check_youtube(name):
    url = f"https://www.youtube.com/@{name}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code == 404:
        return False
    if r.status_code == 200:
        # YouTube serves 200 for both real and nonexistent handles;
        # a real channel page embeds channelMetadataRenderer in its JSON.
        return '"channelMetadataRenderer"' in r.text
    return None

def _check_facebook(name):
    url = f"https://www.facebook.com/{name}"
    r = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
    if r.status_code == 404:
        return False
    if "login" in r.url or "checkpoint" in r.url or r.status_code != 200:
        return None  # hit an auth wall — can't tell from here
    return True

def _check_tiktok(name):
    url = f"https://www.tiktok.com/@{name}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code == 200:
        return True
    if r.status_code == 404:
        return False
    return None


def _check_twitch(name, twitch_client_id=None, twitch_access_token=None):
    if not twitch_client_id or not twitch_access_token:
        raise ValueError(
            "Twitch requires twitch_client_id and twitch_access_token kwargs.\n"
            "1. Register a free app at https://dev.twitch.tv/console\n"
            "2. Get an app access token:\n"
            "   POST https://id.twitch.tv/oauth2/token"
            "?client_id=YOUR_ID&client_secret=YOUR_SECRET&grant_type=client_credentials"
        )
    url = f"https://api.twitch.tv/helix/users?login={name}"
    headers = {
        "Client-Id": twitch_client_id,
        "Authorization": f"Bearer {twitch_access_token}",
    }
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return len(r.json().get("data", [])) > 0

def _check_bluesky(name):
    # Bluesky handles are full domains (e.g. "name.bsky.social"), not bare names
    handle = name if "." in name else f"{name}.bsky.social"
    url = f"https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle={handle}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code == 200:
        return True
    if r.status_code == 400:
        return False  # "Unable to resolve handle"
    return None

def _check_linkedin(name):
    url = f"https://www.linkedin.com/in/{name}"
    r = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
    if r.status_code == 404:
        return False
    if "authwall" in r.url or r.status_code in (999, 403):
        return None  # blocked before we could see anything useful
    return r.status_code == 200

_CHECKERS = {
    "instagram": _check_instagram,
    "youtube": _check_youtube,
    "facebook": _check_facebook,
    "tiktok": _check_tiktok,
    "twitch": _check_twitch,
    "bluesky": _check_bluesky,
    "linkedin": _check_linkedin,
}

def social_availability(name, social, **kwargs):
    social = social.lower().strip()
    name = name.lstrip("@").strip()

    if social not in _CHECKERS:
        raise ValueError(
            f"Unsupported platform '{social}'. Choose from: {', '.join(_CHECKERS)}"
        )

    try:
        taken = _CHECKERS[social](name, **kwargs)
    except Exception as e:
        print(f"[social_availability] error checking {social}/{name}: {e}")
        return None

    if taken is True:
        return unavailable()
    if taken is False:
        return available()
    if taken is None:
        return error()

    print(f"[social_availability] ambiguous result for {social}/{name} — try again later, or check manually")
    return None
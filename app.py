"""
Hello! If you're coming from Streamlit Cloud, please check out the full repository!
I wish the GH icon would take you there instead of here...
"""

import streamlit as st
from utils.tld_availability import tld_availability
from utils.social_availability import social_availability

st.title("Is This Available?", text_alignment = "center")

st.markdown("Check if the name you want is available! Type the name below and hit **Enter**.", text_alignment = "center")

name = st.text_input("Entity", None, label_visibility = "collapsed")

if name != None and name != "":

    st.header("Domains", divider = "rainbow")

    with st.container(horizontal=True):

        tld = [".com", ".net", ".org", ".ai", ".io", ".xyz", ".dev"]

        col1, col2 = st.columns(2)

        with col1:
            for ext in tld:
                st.write(f"{name}{ext}")

        with col2:
            for ext in tld:
                tld_availability(f"{name}{ext}")

    st.header("Socials", divider = "rainbow")

    with st.container(horizontal=True):

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Instagram")
            st.write(f"YouTube")
            st.write(f"Facebook")
            st.write(f"TikTok")
            st.write(f"Twitch")
            st.write(f"Bluesky")
            st.write(f"LinkedIn")

        with col2:
            social_availability(name, "instagram")
            social_availability(name, "youtube")
            social_availability(name, "facebook")
            social_availability(name, "tiktok")
            social_availability(name, "twitch")
            social_availability(name, "bluesky")
            social_availability(name, "linkedin")
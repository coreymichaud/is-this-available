import streamlit as st

st.title("Is This Available?", text_alignment = "center")

st.markdown("Check if the name you want is available! Enter the name below and hit **Enter**.", text_alignment = "center")

name = st.text_input("Entity", None, label_visibility = "collapsed")

if name != None and name != "":

    st.header("Domains", divider = "rainbow")

    col1, col2 = st.columns(2)

    def available():
        st.markdown(":color[**Available!**]{foreground = 'green'}", text_alignment = "right", width = "stretch")
    
    def unavailable():
        st.markdown(":color[**Not Available!**]{foreground = 'red'}", text_alignment = "right", width = "stretch")

    with st.container(horizontal=True):

        with col1:
            st.write(f"{name}.com")
            st.write(f"{name}.net")
            st.write(f"{name}.org")
            st.write(f"{name}.ai")
            st.write(f"{name}.io")
            st.write(f"{name}.xyz")
            st.write(f"{name}.dev")

        with col2:
            available()
            unavailable()
            available()
            unavailable()
            available()
            unavailable()
            unavailable()
    
    st.header("Socials", divider = "rainbow")

    col1, col2 = st.columns(2)

    with st.container(horizontal=True):

        with col1:
            st.write(f"Instagram")
            st.write(f"YouTube")
            st.write(f"Facebook")
            st.write(f"TikTok")
            st.write(f"Twitch")
            st.write(f"Bluesky")
            st.write(f"LinkedIn")

        with col2:
            available()
            unavailable()
            available()
            unavailable()
            available()
            unavailable()
            unavailable()
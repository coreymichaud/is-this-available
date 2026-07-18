import subprocess
import streamlit as st

def available():
    st.markdown(":color[**Available!**]{foreground = 'green'}", text_alignment = "right", width = "stretch")
    
def unavailable():
    st.markdown(":color[**Not Available!**]{foreground = 'red'}", text_alignment = "right", width = "stretch")

def availability(name):
    result = subprocess.run(["dig", "NS", name, "+short"], capture_output=True, text=True)

    if result.stdout.strip() != '':
        return unavailable()
    else:
        return available()
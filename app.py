import pandas as pd
import streamlit as st

with st.sidebar:
    st.image("https://e7.pngegg.com/pngimages/663/591/png-clipart-nba-logo-nba-logo-icons-logos-emojis-iconic-brands-thumbnail.png")
    st.title("AutoStreamML")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])

st.write("Hello World")

import streamlit as st

st.title("Testing camera for tab/mobile")


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
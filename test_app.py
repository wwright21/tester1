import streamlit as st

st.header("I'm awake!")

# add a simple streamlit radio button widget
choice = st.radio("Pick a number", [1, 2, 3])

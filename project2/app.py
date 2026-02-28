import streamlit as st

is_clicked = st.button('Click me')

if is_clicked:
    st.badge('Success')
    
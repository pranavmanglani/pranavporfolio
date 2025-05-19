import streamlit as st

name = "Pranav Manglani"
def change_name():
    name = "changed"
st.button("Change name",onclick=changename())

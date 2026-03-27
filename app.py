import streamlit as st
from helpers.download_models import download_models

def main():
    download_models()
    st.switch_page("pages/home.py")
    
main()

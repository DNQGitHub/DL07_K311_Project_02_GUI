import streamlit as st
from helpers.recommendation.download_models import download_models as download_recommendation_models
from helpers.clustering.download_models import download_models as download_clustering_models

def main():
    download_recommendation_models()
    download_clustering_models()
    st.switch_page("pages/home.py")
    
main()

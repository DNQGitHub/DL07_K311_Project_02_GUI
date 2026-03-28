import streamlit as st
from features.recommendation.helpers.download_models import download_models as download_recommendation_models
from features.clustering.helpers.download_models import download_models as download_clustering_models

def main():
    download_recommendation_models()
    download_clustering_models()
    st.switch_page("pages/home.py")
    
main()

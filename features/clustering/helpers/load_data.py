import streamlit as st
import pandas as pd
import pickle

CLUSTERING_DATA_PATH = "features/clustering/data/data_modeling.parquet"
CLUSTERING_MODEL_PATH = 'features/clustering/models/spectral_clustering_model.pkl'

@st.cache_data
def load_clustering_data():
    df = pd.read_parquet(CLUSTERING_DATA_PATH)
    return df

@st.cache_resource
def load_clustering_model():
    model = pickle.load(open(CLUSTERING_MODEL_PATH, 'rb'))
    return model
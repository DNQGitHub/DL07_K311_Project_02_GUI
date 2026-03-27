import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle


RECOMMENDATION_DATA_PATH = "data/recommendation/dataset_cleaned.parquet"
RECOMMENDATION_STOPWORDS_PATH = "data/recommendation/stopwords.txt"
RECOMMENDATION_SIM_MATRIX_PATH = "models/recommendation/sim_matrix_sentence_transformer.pkl"
RECOMMENDATION_MODEL_PATH = 'models/recommendation/sentence_transformer_model.pkl'
RECOMMENDATION_EMBEDDINGS_PATH = 'models/recommendation/sentence_transformer_embeddings.pkl'

@st.cache_data
def load_recommendation_data():
    df = pd.read_parquet(RECOMMENDATION_DATA_PATH)
    
    scaler = MinMaxScaler()
    df["gia_scaled"] = scaler.fit_transform(df[["gia_ban_num"]])
    
    return df

@st.cache_data
def load_recommendation_sim_matrix():
    return pickle.load(open(RECOMMENDATION_SIM_MATRIX_PATH, "rb"))

@st.cache_data
def load_recommendation_stopwords():
    with open(RECOMMENDATION_STOPWORDS_PATH, 'r', encoding='utf-8') as file:
        stopwords = file.read().split('\n')
    return stopwords

@st.cache_data
def load_recommendation_model():
    model = pickle.load(open(RECOMMENDATION_MODEL_PATH, 'rb'))
    return model

@st.cache_data
def load_recommendation_embeddings():
    embeddings = pickle.load(open(RECOMMENDATION_EMBEDDINGS_PATH, 'rb'))
    return embeddings
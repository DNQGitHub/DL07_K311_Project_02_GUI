import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle


DATA_PATH = "data/dataset_cleaned.parquet"
SIM_MATRIX_PATH = "models/recommendation/sim_matrix_sentence_transformer.pkl"
STOPWORDS_PATH = "data/stopwords.txt"
RECOMMENDATION_MODEL_PATH = 'models/recommendation/sentence_transformer_model.pkl'
RECOMMENDATION_EMBEDDINGS_PATH = 'models/recommendation/sentence_transformer_embeddings.pkl'

@st.cache_data
def load_data():
    df = pd.read_parquet(DATA_PATH)
    
    scaler = MinMaxScaler()
    df["gia_scaled"] = scaler.fit_transform(df[["gia_ban_num"]])
    
    return df

@st.cache_data
def load_sim_matrix():
    return pickle.load(open(SIM_MATRIX_PATH, "rb"))

@st.cache_data
def load_stopwords():
    with open(STOPWORDS_PATH, 'r', encoding='utf-8') as file:
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
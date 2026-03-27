import streamlit as st
import gdown
import os
from tool_scripts.join_file import join_files

SENTENCE_TRANSFORMER_MODEL_DRIVE_URL = 'https://drive.google.com/file/d/1kwB0OiI6NF5noqcdFx31XbvOFf3qr51h/view?usp=drive_link'
SENTENCE_TRANSFORMER_EMBEDDING_DRIVE_URL = 'https://drive.google.com/file/d/1lwjvkdgopOg5ioQ9j3NGWIKF1IbbBROP/view?usp=drive_link'
SIM_MATRIX_SENTENCE_TRANSFORMER_DRIVE_URL = 'https://drive.google.com/file/d/1iK-HByrd5YPt8-On4XPKHDpuMQUMUTSd/view?usp=drive_link'

SENTENCE_TRANSFORMER_MODEL_FILE_ID = '1kwB0OiI6NF5noqcdFx31XbvOFf3qr51h'
SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID = '1lwjvkdgopOg5ioQ9j3NGWIKF1IbbBROP'
SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID = '1iK-HByrd5YPt8-On4XPKHDpuMQUMUTSd'

SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH = 'models/recommendation/sentence_transformer_model.pkl'
SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH = 'models/recommendation/sentence_transformer_embedding.pkl'
SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH = 'models/recommendation/sim_matrix_sentence_transformer.pkl'


def download_models():
    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_MODEL_FILE_ID, output=SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH, quiet=False)

    if not os.path.exists(SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID, output=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH, quiet=False)

    if not os.path.exists(SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH):
        gdown.download(id=SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID, output=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH, quiet=False)

def join_models():
    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH):
        join_files(
            dest_path=SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH, 
            chunk_folder="models/recommendation/chunked/sentence_transformer_model")
    
    if not os.path.exists(SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH):
        join_files(
            dest_path=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH, 
            chunk_folder="models/recommendation/chunked/sentence_transformer_embeddings")
    
    if not os.path.exists(SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH):
        join_files(
            dest_path=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH, 
            chunk_folder="models/recommendation/chunked/sim_matrix_sentence_transformer")

def main():
    download_models()
    st.switch_page("pages/home.py")
    
main()

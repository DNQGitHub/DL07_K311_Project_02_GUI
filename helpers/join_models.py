import os
from helpers.join_file import join_files

SENTENCE_TRANSFORMER_MODEL_LOCAL_CHUNK_FOLDER = 'models/recommendation/chunked/sentence_transformer_model'
SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_CHUNK_FOLDER = 'models/recommendation/chunked/sentence_transformer_embeddings'
SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_CHUNK_FOLDER = 'models/recommendation/chunked/sim_matrix_sentence_transformer'

SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH = 'models/recommendation/sentence_transformer_model.pkl'
SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH = 'models/recommendation/sentence_transformer_embeddings.pkl'
SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH = 'models/recommendation/sim_matrix_sentence_transformer.pkl'

def join_models():
    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH):
        join_files(
            dest_path=SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH, 
            chunk_folder=SENTENCE_TRANSFORMER_MODEL_LOCAL_CHUNK_FOLDER)
    
    if not os.path.exists(SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH):
        join_files(
            dest_path=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH, 
            chunk_folder=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_CHUNK_FOLDER)
    
    if not os.path.exists(SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH):
        join_files(
            dest_path=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH, 
            chunk_folder=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_CHUNK_FOLDER)

import os
from helpers.join_file import join_files

SPECTRAL_CLUSTERING_MODEL_LOCAL_CHUNK_FOLDER = 'features/clustering/models/chunked/spectral_clustering_model'
SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH = 'features/clustering/models/spectral_clustering_model.pkl'

def join_models():
    if not os.path.exists(SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH):
        join_files(
            dest_path=SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH, 
            chunk_folder=SPECTRAL_CLUSTERING_MODEL_LOCAL_CHUNK_FOLDER)

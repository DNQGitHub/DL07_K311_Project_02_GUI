import os
import gdown

SPECTRAL_CLUSTERING_MODEL_FILE_ID = '1R9DD6BFpouHFzfXGpud9B9Og9iF5g9Wh'
SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH = 'features/clustering/models/spectral_clustering_model.pkl'

def download_models():
    if not os.path.exists(SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH):
        gdown.download(id=SPECTRAL_CLUSTERING_MODEL_FILE_ID, output=SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH, quiet=False)

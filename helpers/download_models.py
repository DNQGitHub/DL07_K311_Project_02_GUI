import os
import gdown

# --RECOMMENDATION--------------
SENTENCE_TRANSFORMER_MODEL_FILE_ID = '1kwB0OiI6NF5noqcdFx31XbvOFf3qr51h'
SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID = '1lwjvkdgopOg5ioQ9j3NGWIKF1IbbBROP'
SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID = '1iK-HByrd5YPt8-On4XPKHDpuMQUMUTSd'

SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH = 'models/recommendation/sentence_transformer_model.pkl'
SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH = 'models/recommendation/sentence_transformer_embeddings.pkl'
SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH = 'models/recommendation/sim_matrix_sentence_transformer.pkl'

# --CLUSTERING--------------
SPECTRAL_CLUSTERING_MODEL_FILE_ID = '1R9DD6BFpouHFzfXGpud9B9Og9iF5g9Wh'
SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH = 'models/clustering/spectral_clustering_model.pkl'

def download_models():
    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_MODEL_FILE_ID, output=SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH, quiet=False)

    if not os.path.exists(SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID, output=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH, quiet=False)

    if not os.path.exists(SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH):
        gdown.download(id=SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID, output=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH, quiet=False)

    if not os.path.exists(SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH):
        gdown.download(id=SPECTRAL_CLUSTERING_MODEL_FILE_ID, output=SPECTRAL_CLUSTERING_MODEL_LOCAL_PATH, quiet=False)

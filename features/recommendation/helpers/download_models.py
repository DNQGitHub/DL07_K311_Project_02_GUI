import os
import gdown

SENTENCE_TRANSFORMER_MODEL_FILE_ID = '1kwB0OiI6NF5noqcdFx31XbvOFf3qr51h'
SENTENCE_TRANSFORMER_MODEL_HALF_FILE_ID = '1eqfxIgH4agNeyUyoOFwgQBHl3FfQntZW'
SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID = '1lwjvkdgopOg5ioQ9j3NGWIKF1IbbBROP'
SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID = '1iK-HByrd5YPt8-On4XPKHDpuMQUMUTSd'

SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH = 'features/recommendation/models/sentence_transformer_model.pkl'
SENTENCE_TRANSFORMER_MODEL_HALF_LOCAL_PATH = 'features/recommendation/models/sentence_transformer_model_half.pkl'
SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH = 'features/recommendation/models/sentence_transformer_embeddings.pkl'
SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH = 'features/recommendation/models/sim_matrix_sentence_transformer.pkl'

def download_models():
    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_MODEL_FILE_ID, output=SENTENCE_TRANSFORMER_MODEL_LOCAL_PATH, quiet=False)

    if not os.path.exists(SENTENCE_TRANSFORMER_MODEL_HALF_LOCAL_PATH):
        gdown.download_folder(id=SENTENCE_TRANSFORMER_MODEL_HALF_FILE_ID, output=SENTENCE_TRANSFORMER_MODEL_HALF_LOCAL_PATH, quiet=False)

    if not os.path.exists(SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH):
        gdown.download(id=SENTENCE_TRANSFORMER_EMBEDDING_FILE_ID, output=SENTENCE_TRANSFORMER_EMBEDDING_LOCAL_PATH, quiet=False)

    if not os.path.exists(SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH):
        gdown.download(id=SIM_MATRIX_SENTENCE_TRANSFORMER_FILE_ID, output=SIM_MATRIX_SENTENCE_TRANSFORMER_LOCAL_PATH, quiet=False)

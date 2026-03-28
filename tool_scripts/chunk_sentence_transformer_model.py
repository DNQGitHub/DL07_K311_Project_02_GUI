import sys
import os
sys.path.insert(0, os.getcwd())

from helpers.chunk_file import chunk_file

chunk_file(
    source_path='models/recommendation/sentence_transformer_model.pkl',
    chunk_size=24*1024*1024,
    dest_folder="models/recommendation/chunked/sentence_transformer_model",
    dest_file_pattern='{0}.bin')
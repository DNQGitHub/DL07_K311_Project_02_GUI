import sys
import os
sys.path.insert(0, os.getcwd())

from helpers.chunk_file import chunk_file

if __name__ == "__main__":
    chunk_file(
        source_path='features/recommendation/models/_backup/sentence_transformer_embeddings.pkl',
        chunk_size=24*1024*1024,
        dest_folder="features/recommendation/models/chunked/sentence_transformer_embeddings",
        dest_file_pattern='{0}.bin')
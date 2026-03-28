import sys
import os
sys.path.insert(0, os.getcwd())

from helpers.chunk_file import chunk_file

chunk_file(
    source_path='features/clustering/models/_backup/spectral_clustering_model.pkl',
    chunk_size=24*1024*1024,
    dest_folder="features/clustering/models/chunked/spectral_clustering_model",
    dest_file_pattern='{0}.bin')
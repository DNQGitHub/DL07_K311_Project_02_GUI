import sys
import os
sys.path.insert(0, os.getcwd())

from helpers.chunk_file import chunk_file

chunk_file(
    source_path='models/recommendation/sim_matrix_sentence_transformer.pkl',
    chunk_size=24*1024*1024,
    dest_folder="models/recommendation/chunked/sim_matrix_sentence_transformer",
    dest_file_pattern='{0}.bin')
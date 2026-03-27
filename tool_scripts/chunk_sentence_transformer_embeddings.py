from helpers.chunk_file import chunk_file

chunk_file(
    source_path='models/recommendation/sentence_transformer_embeddings.pkl',
    chunk_size=24*1024*1024,
    dest_folder="models/recommendation/chunked/sentence_transformer_embeddings",
    dest_file_pattern='{0}.bin')
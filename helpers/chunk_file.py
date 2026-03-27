import os

def chunk_file(source_path, chunk_size, dest_folder='chunks', dest_file_pattern='model_{0}.bin'):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        
    index = 0
    with open(source_path, 'rb') as infile:
        while True:
            chunk_data = infile.read(chunk_size)
            if not chunk_data:
                break
            chunk_filename = os.path.join(dest_folder, dest_file_pattern.format(index))
            with open(chunk_filename, 'wb') as outfile:
                outfile.write(chunk_data)
            index += 1
    print(f"Split {source_path} into {index} chunks in '{dest_folder}'.")
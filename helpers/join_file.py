import os

def join_files(dest_path, chunk_prefix='', chunk_folder='chunks'):
    with open(dest_path, 'wb') as outfile:
        index = 0
        while True:
            chunk_filename = os.path.join(chunk_folder, f'{chunk_prefix}{index:03d}.bin')
            try:
                with open(chunk_filename, 'rb') as infile:
                    outfile.write(infile.read())
                index += 1
            except FileNotFoundError:
                break
    print(f"Recombined {index} chunks into {dest_path}.")



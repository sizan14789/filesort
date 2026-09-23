from pathlib import Path
from setup import SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, IMAGES, AUDIO, videos_path, software_path, documents_path, compressed_path, images_path, audios_path, create_base
from zip_handler import handle_zip
from moving_methods import move_file

# handle every file
def handle_file(file: Path) -> None:
    create_base()
    dest_folder = None 

    if file.name.lower().endswith(SOFTWARE):
        dest_folder = software_path
    elif file.name.lower().endswith(COMPRESSED):
        dest_folder = compressed_path
    elif file.name.lower().endswith(VIDEOS): # to be handled later in depth
        dest_folder = videos_path
    elif file.name.lower().endswith(DOCUMENTS):
        dest_folder = documents_path
    elif file.name.lower().endswith(IMAGES):
        dest_folder = images_path
    elif file.name.lower().endswith(AUDIO):
        dest_folder = audios_path

    if dest_folder:
        move_file(file, dest_folder)
        return
    
    if file.name.lower().endswith(".zip"):
        handle_zip(file)

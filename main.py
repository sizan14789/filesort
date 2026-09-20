from pathlib import Path
from setup import prod, single_instance, BASE, SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, IMAGES, AUDIO, videos_path, software_path, documents_path, compressed_path, images_path, audios_path, create_base
from zip_handler import handle_zip
from methods import move_file

# handle every file
def handle_file(file: Path) -> None:
    create_base()
    dest_folder = None 

    if file.name.endswith(SOFTWARE):
        dest_folder = software_path
    elif file.name.endswith(COMPRESSED):
        dest_folder = compressed_path
    elif file.name.endswith(VIDEOS): # to be handled later in depth
        dest_folder = videos_path
    elif file.name.endswith(DOCUMENTS):
        dest_folder = documents_path
    elif file.name.endswith(IMAGES):
        dest_folder = images_path
    elif file.name.endswith(AUDIO):
        dest_folder = audios_path

    if dest_folder:
        move_file(file, dest_folder)
        return
    
    if file.name.endswith(".zip"):
        handle_zip(file)

# sorting previous files before watchdog starts
def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

if prod and single_instance:
    print(f"Sorting {BASE}...")

sort_all_once()

if prod and single_instance:
    print("Done!")
    input()

if single_instance:
    exit()

# watchdog from here


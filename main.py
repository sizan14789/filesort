from pathlib import Path
from paths_types import prod, single_instance, BASE, SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, IMAGES, AUDIO, videos_path, software_path, documents_path, compressed_path, images_path, audios_path, create_base
from zip_handler import handle_zip

# takes file and destination, checks if duplicate exists, renames and moves
def check_dest_move(file: Path, dest_folder: Path) -> None:
    dest = dest_folder / file.name
    i = 1
    while dest.exists():
        dest = dest_folder / f"{file.stem}({i}){file.suffix}"
        i+=1
    
    file.rename(dest)

# handle every file
def handle_file(file: Path) -> None:
    create_base()
    dest_folder = None

    file_type = file.suffix

    if file_type in SOFTWARE:
        dest_folder = software_path
    elif file_type in COMPRESSED:
        dest_folder = compressed_path
    elif file_type in VIDEOS: # to be handled later in depth
        dest_folder = videos_path
    elif file_type in DOCUMENTS:
        dest_folder = documents_path
    elif file_type in IMAGES:
        dest_folder = images_path
    elif file_type in AUDIO:
        dest_folder = audios_path

    if dest_folder:
        check_dest_move(file, dest_folder)
        return
    
    if file.suffix == ".zip":
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


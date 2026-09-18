from pathlib import Path
from paths_types import BASE, SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, videos_path, software_path, documents_path, compressed_path, create_base
from zip_handler import handle_zip

def handle_file(file) -> None:
    create_base()
    destination = None

    file_type = file.suffix

    if file_type in SOFTWARE:
        destination = software_path
    elif file_type in COMPRESSED:
        destination = compressed_path
    elif file_type in VIDEOS: # to be handled later in depth
        destination = videos_path
    elif file_type in DOCUMENTS:
        destination = documents_path

    if destination:
        file.rename(destination / file.name)
        return
    
    if file.suffix ==".zip":
        handle_zip(file)
    
for file in BASE.iterdir():
    if file.is_file():
        handle_file(file)


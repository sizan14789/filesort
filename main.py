from pathlib import Path
from paths_types import BASE, SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, videos_path, software_path, documents_path, compressed_path, create_base
from zip_handler import handle_zip

def handle_file(file) -> None:
    create_base()
    dest = None

    file_type = file.suffix

    if file_type in SOFTWARE:
        dest = software_path
    elif file_type in COMPRESSED:
        dest = compressed_path
    elif file_type in VIDEOS: # to be handled later in depth
        dest = videos_path
    elif file_type in DOCUMENTS:
        dest = documents_path

    if dest:
        file.rename(dest / file.name)
        return
    
    if file.suffix ==".zip":
        handle_zip(file)
    
for file in BASE.iterdir():
    if file.is_file():
        handle_file(file)

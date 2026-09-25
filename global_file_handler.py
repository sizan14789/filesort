from pathlib import Path
from time import sleep

# local imports
from app_context import SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS, IMAGES, AUDIO, videos_path, software_path, documents_path, compressed_path, images_path, audios_path, create_base
import app_context
from zip_handler import handle_zip
from app_context import move_file

# waits till the file is readable to avoid moving a file thats being transferred, if transfer fails/stops midway...returns false to ignore the file
def wait_till_ready(file: Path) -> bool:
    while 1:
        try:
            with open(file, 'rb'):
                return True
        except PermissionError:
            sleep(1)
        except FileNotFoundError:
            return False

# handle a file
def handle_file(file: Path) -> None:
    if app_context.paused or not file.exists(): 
        return

    # wait till download/copying finishes, if file disappears before ignore it
    if not wait_till_ready(file):
        return
    
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

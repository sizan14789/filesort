from pathlib import Path
from lib import SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS
from zipfile import ZipFile
import shutil

BASE = Path.cwd()

# wallpaper, images, audio left
videos_path = BASE / "videos"
software_path = BASE / "software"
documents_path = BASE / "documents"
compressed_path = BASE / "compressed"
zip_path = BASE / "zip"

def create_base():
    videos_path.mkdir(exist_ok=True)
    software_path.mkdir(exist_ok=True)
    documents_path.mkdir(exist_ok=True)
    compressed_path.mkdir(exist_ok=True)
    zip_path.mkdir(exist_ok=True)

def get_name_parts(zip_element_info) -> tuple[str, str]:
    as_path = Path(zip_element_info.filename) 
    return as_path.stem, as_path.suffix
      
def unzip_to_videos_nested(root_file): 
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    with ZipFile(root_file, 'r') as z:
        for info in z.infolist():
            if info.is_dir():
                continue

            # get nonexisting file name
            p1, p2 = get_name_parts(info)
            initial_file_name = final_file_name = p1 + p2
            
            i = 1
            while (videos_path / final_file_name).exists():
                final_file_name = f"{p1}({i}){p2}"
                i+=1

            extracted = Path(z.extract(info, temp_folder))
            extracted.rename(videos_path / final_file_name)

    shutil.rmtree(temp_folder)

def unzip_to_new(zip_file):
    new_folder_path = videos_path / zip_file.stem

    i = 1
    while new_folder_path.exists():
        new_folder_path = videos_path / (f"{zip_file.stem}({i})")
        i+=1
    new_folder_path.mkdir(exist_ok=True)

    if new_folder_path.exists():
        with ZipFile(zip_file, 'r') as z:
            z.extractall(new_folder_path)

def unzip_to_videos(root_file):
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    with ZipFile(root_file, 'r') as z:
        z.extractall(temp_folder)
     
    for folder in temp_folder.iterdir():
        folder_destination = videos_path / folder.name
        
        i = 1
        while folder_destination.exists():
            folder_destination = videos_path / (f"{folder.stem}({i}){folder.suffix}")
            i+=1
        
        folder.rename(folder_destination)

    temp_folder.rmdir()

def handle_zip(zip_file): 
    # parameter gathering for decision making
    top_level_video_count = videos_count = other_file_count = 0
    with ZipFile(zip_file, 'r') as z:
        all_zip_files = [Path(info.filename) for info in z.infolist()]
        top_level_files = [path for path in all_zip_files if len(path.parts)==1]

        # detect if top level contains any videos
        top_level_video_count = sum(file.suffix in VIDEOS for file in top_level_files)
        
        # Count videos to know if its a series
        videos_count = other_file_count = 0
        for path in all_zip_files:
            if path.is_dir():
                continue
            if path.suffix in VIDEOS:
                videos_count+=1
            else: 
                other_file_count+=1

    # decision making 
    if other_file_count > videos_count or not videos_count:
        zip_file.rename(zip_path / zip_file.name)
        return

    if videos_count==1: # single movie or nested movies inside inside folder so get it
        unzip_to_videos_nested(zip_file)
    elif not top_level_video_count: # series inside folder so directly unzip to videos
        unzip_to_videos(zip_file)
    else: # series
        unzip_to_new(zip_file)
    
    # handle the remaining zip 
    zip_file.rename(zip_path / zip_file.name)

def handle_static(file) -> None:
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
        handle_static(file)







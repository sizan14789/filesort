from pathlib import Path
from lib import SOFTWARE, COMPRESSED, VIDEOS, DOCUMENTS
import zipfile

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

def unzip_to_new(zip_file):
    new_folder_path = videos_path / zip_file.stem

    i = 1
    while new_folder_path.exists():
        new_folder_path = videos_path / (zip_file.stem + str(i))
        i+=1
    new_folder_path.mkdir(exist_ok=True)

    if new_folder_path.exists():
        with zipfile.ZipFile(zip_file, 'r') as z:
            z.extractall(new_folder_path)
    
def get_name_parts(zip_element_info):
    name_splitted_list = zip_element_info.filename.split(".")
    first_part = ""
    second_part = "." + name_splitted_list[-1]
    name_splitted_list.pop()

    for i, s in enumerate(name_splitted_list):
        if i!=len(name_splitted_list)-1:
            first_part+= s + "."  
    
    return first_part, second_part

def unzip_to_videos(root_file):
    videos_folder_file_list = {Path(v).name for v in videos_path.iterdir()}

    with zipfile.ZipFile(root_file, 'r') as z:
        for info in z.infolist():
            # get nonexisting file name
            p1, p2 = get_name_parts(info)
            file_name = p1 + p2
            i = 1
            while True:
                if file_name not in videos_folder_file_list:
                    break
                file_name = p1 + str(i) + p2
                i+=1
            
            print(file_name)
            # extract
            # z.extract(info)

def move_zip(root_file):
    pass

def handle_zip(zip_file): 
    # parameter gathering for decision making
    top_level_video_count = videos_count = other_file_count = 0
    with zipfile.ZipFile(zip_file, 'r') as z:
        all_zip_files  = [Path(info.filename) for info in z.infolist()]
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
        move_zip(zip_file)
        return

    if not top_level_video_count:
        if videos_count==1: # single movie inside folder so get it
            pass
        else: # series inside folder so directly unzip to videos
            unzip_to_videos(zip_file)
    else:
        if videos_count==1: # single movie zip
            unzip_to_videos(zip_file)
        else: # series
            unzip_to_new(zip_file)
    
    # handle the remaining zip 
    move_zip(zip_file)

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







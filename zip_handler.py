from pathlib import Path
from paths_types import BASE, VIDEOS, videos_path, zip_path, extracted_zip_path
from zipfile import ZipFile
import shutil

# move zip
def move_zip(zip_file, dest_path):
    dest = dest_path / zip_file.name
    i = 1
    while dest.exists():
        dest = dest_path / (f"{zip_file.stem}({i}){zip_file.suffix}")
        i+=1
    zip_file.rename(dest)

# extracts the videos, nested or rooted, and moves them to videos
def unzip_to_videos_nested(zip_file): 
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    with ZipFile(zip_file, 'r') as z:
        for info in z.infolist():
            if info.is_dir(): # ignore folders
                continue

            # get nonexisting file name using Path
            as_path = Path(info.filename)
            p1, p2 = as_path.stem, as_path.suffix
            initial_file_name = final_file_name = p1 + p2
            
            i = 1
            while (videos_path / final_file_name).exists():
                final_file_name = f"{p1}({i}){p2}"
                i+=1

            # extract and move
            extracted = Path(z.extract(info, temp_folder))
            extracted.rename(videos_path / final_file_name)

    shutil.rmtree(temp_folder)

# extracts the entire zip content to a new folder and moves it to videos
def unzip_to_new(zip_file):
    # find nonexisting folder name inside videos
    new_folder_path = videos_path / zip_file.stem
    i = 1
    while new_folder_path.exists():
        new_folder_path = videos_path / (f"{zip_file.stem}({i})")
        i+=1
    
    # create and extract to new folder
    new_folder_path.mkdir(exist_ok=True)
    if new_folder_path.exists():
        with ZipFile(zip_file, 'r') as z:
            z.extractall(new_folder_path)

# extracts the entire zip content directly to videos
def unzip_to_videos(zip_file):
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    # extract all to temp
    with ZipFile(zip_file, 'r') as z:
        z.extractall(temp_folder)
     
    # move, rename if file already exists
    for folder in temp_folder.iterdir():
        folder_destination = videos_path / folder.name
        
        i = 1
        while folder_destination.exists():
            folder_destination = videos_path / (f"{folder.stem}({i}){folder.suffix}")
            i+=1
        
        folder.rename(folder_destination)

    temp_folder.rmdir()

# handles the zip, including the decision making process
def handle_zip(zip_file): 
    # parameter gathering for decision making
    top_level_video_count = videos_count = other_file_count = 0
    with ZipFile(zip_file, 'r') as z:
        all_zip_files = [Path(info.filename) for info in z.infolist()]
        top_level_files = [path for path in all_zip_files if len(path.parts)==1]

        # count top level videos
        top_level_video_count = sum(file.suffix in VIDEOS for file in top_level_files)
        
        # Count videos
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
        move_zip(zip_file, zip_path)
        return

    # rooted / nested movie
    if videos_count==1: 
        unzip_to_videos_nested(zip_file)

    # nested series 
    elif not top_level_video_count: 
        unzip_to_videos(zip_file)

    # rooted series or nested+rooted video mix
    else: 
        unzip_to_new(zip_file)
    
    # move the remaining zip 
    move_zip(zip_file, extracted_zip_path)

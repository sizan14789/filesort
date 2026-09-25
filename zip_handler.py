from pathlib import Path
from shutil import rmtree

# local imports
from app_context import BASE, VIDEOS, videos_path, zip_path, extracted_zip_path
from zipfile import ZipFile, is_zipfile
from app_context import move_file, get_unique_dest

# extracts videos, nested or rooted, and moves them to videos
def unzip_to_videos_nested(zip_file): 
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    with ZipFile(zip_file, 'r') as z:
        for info in z.infolist():
            if info.is_dir(): # ignore folders
                continue

            # extract and move
            extracted = Path(z.extract(info, temp_folder))
            extracted.rename(get_unique_dest(extracted, videos_path))

    rmtree(temp_folder)

# extracts zip contents to a new folder and moves it to videos
def unzip_to_new(zip_file):
    new_folder_path = get_unique_dest(zip_file.parent / zip_file.stem, videos_path)
    
    # create and extract to new folder
    new_folder_path.mkdir(exist_ok=True) 
    with ZipFile(zip_file, 'r') as z:
        z.extractall(new_folder_path)

# extracts zip contents directly to videos
def unzip_to_videos(zip_file):
    temp_folder = BASE / "temp"
    temp_folder.mkdir(exist_ok = True)

    # extract all to temp
    with ZipFile(zip_file, 'r') as z:
        z.extractall(temp_folder)
     
    # move, rename if file already exists
    for folder in temp_folder.iterdir():
        # folder_destination = videos_path / folder.name
        
        # i = 1
        # while folder_destination.exists():
        #     folder_destination = videos_path / (f"{folder.stem}({i}){folder.suffix}")
        #     i+=1
        
        folder.rename(get_unique_dest(folder, videos_path))

    temp_folder.rmdir()

# handles zip files, including the decision making process
def handle_zip(zip_file): 
    if not is_zipfile(zip_file):
        return
    
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
            if path.name.lower().endswith(VIDEOS):
                videos_count+=1
            else: 
                other_file_count+=1

    # decision making 
    if other_file_count > videos_count or not videos_count:
        move_file(zip_file, zip_path)
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
    move_file(zip_file, extracted_zip_path)

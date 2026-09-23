from pathlib import Path

# takes file path and destination, checks if duplicate exists, returns and unique address
def get_unique_dest(file: Path, dest_folder: Path) -> Path:
    dest = dest_folder / file.name
    i = 1
    while dest.exists():
        dest = dest_folder / f"{file.stem}({i}){file.suffix}"
        i+=1
    
    return dest

# takes file path and destination, moves files
def move_file(file, dest_folder):
    file.rename(get_unique_dest(file, dest_folder))
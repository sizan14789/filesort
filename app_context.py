from pathlib import Path

prod=1 
paused=0

# Extensions 
SOFTWARE = (
    ".exe", ".msi", ".appx", ".deb", ".rpm", ".dmg",
    ".apk", ".bat", ".cmd", ".sh"
)

COMPRESSED = (
    ".rar", ".7z", ".tar", ".gz", ".bz2",
    ".xz", ".tar.gz", ".tar.bz2", ".tar.xz"
)

VIDEOS = (
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",
    ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".ts"
)

DOCUMENTS = (
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".txt", ".rtf", ".csv", ".odt", ".ods", ".odp"
)

IMAGES = (
    ".jpg", ".jpeg", ".png", ".webp", ".gif",
    ".bmp", ".svg", ".ico", ".tiff", ".tif"
)

AUDIO = (
    ".mp3", ".wav", ".flac", ".aac", ".ogg",
    ".m4a", ".wma", ".opus", ".aiff", ".ape"
)

# production
BASE = Path.home() / "Downloads"

# dev
if not prod:
    BASE = Path.cwd()

# wallpaper, images, audio left
videos_path = BASE / "videos"
software_path = BASE / "software"
documents_path = BASE / "documents"
compressed_path = BASE / "compressed"
images_path = BASE / "images"
audios_path = BASE / "audios"

extracted_zip_path = compressed_path / "extracted_zips"
zip_path = BASE / "zip"

# creates base folder in  case they don't exist
def create_base():
    videos_path.mkdir(exist_ok=True)
    software_path.mkdir(exist_ok=True)
    documents_path.mkdir(exist_ok=True)
    compressed_path.mkdir(exist_ok=True)
    images_path.mkdir(exist_ok=True)
    audios_path.mkdir(exist_ok=True)
    zip_path.mkdir(exist_ok=True)
    extracted_zip_path.mkdir(exist_ok=True)

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
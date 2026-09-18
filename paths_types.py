from pathlib import Path

SOFTWARE = {
    ".exe", ".msi", ".appx", ".deb", ".rpm", ".dmg",
    ".apk", ".bat", ".cmd", ".sh"
}

COMPRESSED = {
    ".rar", ".7z", ".tar", ".gz", ".bz2",
    ".xz", ".tar.gz", ".tar.bz2", ".tar.xz"
}

VIDEOS = {
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",
    ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".ts"
}

DOCUMENTS = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".txt", ".rtf", ".csv", ".odt", ".ods", ".odp"
}

BASE = Path.cwd()

# wallpaper, images, audio left
videos_path = BASE / "videos"
software_path = BASE / "software"
documents_path = BASE / "documents"
compressed_path = BASE / "compressed"
zip_path = BASE / "zip"

# creates base folder in  case they don't exist
def create_base():
    videos_path.mkdir(exist_ok=True)
    software_path.mkdir(exist_ok=True)
    documents_path.mkdir(exist_ok=True)
    compressed_path.mkdir(exist_ok=True)
    zip_path.mkdir(exist_ok=True)

# FileSort

A Python file organizer for Windows that sorts files in the Downloads folder into separate folders based on their type.

## What it does

FileSort detects common file types and moves them into organized folders. It also handles duplicate filenames and ZIP files containing videos.

### ZIP handling

FileSort inspects the contents of a ZIP before deciding what to do with it:

- **ZIP with more non-video files than videos** → the ZIP is moved to `zip/` without extraction.
- **Single video, whether directly in the ZIP or inside a folder** → the video is extracted to `videos/`.
- **Multiple videos inside a folder** → the ZIP contents are extracted into a new folder inside `videos/`.
- **Multiple videos directly at the ZIP root** → the ZIP contents are extracted into a new folder inside `videos/`.
- **ZIP containing both root-level and nested videos** → the contents are extracted into a new folder inside `videos/`.

After a ZIP is processed, the original ZIP is kept in:

`Downloads/compressed/extracted_zips/`

ZIPs that are not extracted are kept in:

`Downloads/zip/`

**Note:** ZIP extraction is currently supported. Other archive extensions such as `.rar` and `.7z` are recognized as archive files but are not extracted by the current implementation.

## Installation

### Requirements

- Windows
- Python 3.10+

Clone the repository:

```
git clone <repository-url>
cd FileSort
```

Run the program:

```
python main.py
```

**Downloads folder:** FileSort works with the standard default Downloads folder on Windows, Linux, and macOS. If your Downloads folder has been moved to another location, such as OneDrive or another drive, FileSort may not detect it correctly.

## Folder Structure

Downloads/\
├── videos/\
├── documents/\
├── images/\
├── audios/\
├── software/\
├── compressed/\
│ └── extracted_zips/\
└── zip/

## Supported Formats

**Videos:** `mp4`, `mkv`, `avi`, `mov`, `wmv`, `flv`, `webm`, `m4v`, `mpeg`, `mpg`, `3gp`, `ts`

**Images:** `jpg`, `jpeg`, `png`, `webp`, `gif`, `bmp`, `svg`, `ico`, `tiff`, `tif`

**Audio:** `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`, `wma`, `opus`, `aiff`, `ape`

**Documents:** `pdf`, `doc`, `docx`, `xls`, `xlsx`, `ppt`, `pptx`, `txt`, `rtf`, `csv`, `odt`, `ods`, `odp`

**Software:** `exe`, `msi`, `appx`, `deb`, `rpm`, `dmg`, `apk`, `bat`, `cmd`, `sh`

**Archives:** `zip`, `rar`, `7z`, `tar`, `gz`, `bz2`, `xz`

## Important

FileSort moves files out of the Downloads folder and extracts selected ZIP contents. Make sure you understand the sorting rules before running it on important files.

## Current Status

Currently, FileSort runs once and sorts the files already present in the Downloads folder.

Planned:

- Background file monitoring with `watchdog`
- System tray support with `pystray`
- Windows startup support
- Smarter video sorting

## Project Structure

FileSort/\
├── main.py\
├── paths_types.py\
├── zip_handler.py\
└── ...

## Tech Stack

- Python
- `pathlib`
- `zipfile`
- `shutil`

## Customization

FileSort is a personal project, but anyone can fork it and make their own version.

You can modify the supported extensions, folder structure, sorting rules, and archive handling to fit your needs.

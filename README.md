# FileSort

A Python file organizer that automatically organizes your Downloads folder and monitors it in the background for new files.

## Problem Statement

The Downloads folder can quickly become cluttered with videos, images, documents, audio, software, and archive files.

FileSort automatically organizes these files into separate folders and handles duplicate filenames and intelligent ZIP extraction.

## Download

Windows users can download the latest installer from the [Releases](https://github.com/sizan14789/filesort/releases) page.

If you prefer the portable version, the standalone executable is also available there.

## Features

- **Automatic File Sorting** — Organizes files in your Downloads folder by type.
- **Background Monitoring** — Automatically detects and sorts newly downloaded or moved files.
- **Duplicate Handling** — Renames files automatically when a file with the same name already exists.
- **ZIP File Processing** — Inspects ZIP files and extracts video content based on the archive structure.
- **Archive Organization** — Keeps processed and unprocessed archive files in separate folders.
- **System Tray Support** — Runs quietly in the background with Pause/Resume and Exit controls.
- **Desktop Notifications** — Notifies you when FileSort starts and when certain archive problems are detected.
- **Single Instance** — Prevents multiple FileSort processes from running at the same time.
- **Windows Startup** — Can start automatically with Windows after installation.
- **Local Processing** — Files are processed locally without uploading them to an external service.

## Supported Extensions

**Videos:** `mp4`, `mkv`, `avi`, `mov`, `wmv`, `flv`, `webm`, `m4v`, `mpeg`, `mpg`, `3gp`, `ts`

**Images:** `jpg`, `jpeg`, `png`, `webp`, `gif`, `bmp`, `svg`, `ico`, `tiff`, `tif`

**Audio:** `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`, `wma`, `opus`, `aiff`, `ape`

**Documents:** `pdf`, `doc`, `docx`, `xls`, `xlsx`, `ppt`, `pptx`, `txt`, `rtf`, `csv`, `odt`, `ods`, `odp`

**Software:** `exe`, `msi`, `appx`, `deb`, `rpm`, `dmg`, `apk`, `bat`, `cmd`, `sh`

**Archives:** `zip`, `rar`, `7z`, `tar`, `gz`, `bz2`, `xz`

## Archive Rules

FileSort recognizes several archive formats, but currently only extracts ZIP files.

- **More non-video files than videos** → archive is moved to `archives/` without extraction.
- **One video** → video is extracted to `videos/`, whether it is at the archive root or inside a folder.
- **Multiple videos inside a folder** → archive contents are extracted into a new folder inside `videos/`.
- **Multiple videos at the archive root** → archive contents are extracted into a new folder inside `videos/`.
- **Root-level and nested videos** → archive contents are extracted into a new folder inside `videos/`.

Processed archive files are kept in:

```text
Downloads/
└── archives/
    └── extracted_archives/
```

Archives that are not extracted are kept in:

```text
Downloads/
└── archives/
```

Only ZIP files are extracted. Other archive formats are recognized and moved to the archive location but are not extracted.

**Exception:** Corrupt/password protected archive files are left untouched.

## Platform Support

### Windows

A ready-to-use Windows executable is available in the releases. See the Startup Setup section below for automatic startup configuration.

### Linux / macOS

No pre-built executable is currently provided. PyInstaller builds are platform-specific, so Linux and macOS executables must be built separately on their respective platforms.

**Follow the installation guide below to build your own executable.**

## Installation

### Requirements

- Python 3.10+
- watchdog
- pystray
- Pillow
- desktop-notifier

Clone the repository:

```bash
git clone https://github.com/sizan14789/filesort.git
cd filesort
```

Install dependencies:

```bash
pip install watchdog pystray pillow desktop-notifier
```

Run:

```bash
python main.py
```

FileSort uses the standard `Downloads` folder of the current user.

### Build Executable

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "FileSort" --icon="assets/icon.ico" --add-data "assets/icon.ico;assets" --collect-all desktop_notifier main.py
```

## Project Structure

```text
FileSort/
├── main.py
├── app_context.py
├── global_file_handler.py
├── zip_handler.py
├── watchman.py
├── system_tray.py
├── toaster.py
├── mutex.py
└── assets/
    └── icon.ico
```

## Privacy

FileSort processes files locally and does not upload or transmit your files.

## Bug Reports

If you find a bug, please open an issue with:

- A description of the problem
- Steps to reproduce it
- Relevant error messages or screenshots
- Your OS and Python version

## Author

**Sizan Molla**

- GitHub: [sizan14789](https://github.com/sizan14789)
- Email: sizanalt@gmail.com

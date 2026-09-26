# FileSort

A Python file organizer that automatically sorts files in your Downloads folder by type.

## Problem Statement

The Downloads folder can quickly become cluttered with videos, images, documents, audio, software, and archive files.

FileSort automatically organizes these files into separate folders and handles duplicate filenames and selected ZIP extraction.

## Supported Extensions

**Videos:** `mp4`, `mkv`, `avi`, `mov`, `wmv`, `flv`, `webm`, `m4v`, `mpeg`, `mpg`, `3gp`, `ts`

**Images:** `jpg`, `jpeg`, `png`, `webp`, `gif`, `bmp`, `svg`, `ico`, `tiff`, `tif`

**Audio:** `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`, `wma`, `opus`, `aiff`, `ape`

**Documents:** `pdf`, `doc`, `docx`, `xls`, `xlsx`, `ppt`, `pptx`, `txt`, `rtf`, `csv`, `odt`, `ods`, `odp`

**Software:** `exe`, `msi`, `appx`, `deb`, `rpm`, `dmg`, `apk`, `bat`, `cmd`, `sh`

**Archives:** `zip`, `rar`, `7z`, `tar`, `gz`, `bz2`, `xz`

## ZIP Rules

FileSort inspects the contents of a ZIP before deciding how to handle it.

- **More non-video files than videos** → ZIP is moved to `zip/` without extraction.
- **One video** → video is extracted to `videos/`, whether it is at the ZIP root or inside a folder.
- **Multiple videos inside a folder** → ZIP contents are extracted into a new folder inside `videos/`.
- **Multiple videos at the ZIP root** → ZIP contents are extracted into a new folder inside `videos/`.
- **Root-level and nested videos** → ZIP contents are extracted into a new folder inside `videos/`.

Processed ZIP files are kept in:

```text
Downloads/
└── compressed/
    └── extracted_zips/
```

ZIP files that are not extracted are kept in:

```text
Downloads/
└── zip/
```

Only ZIP files are extracted. Other archive formats are recognized and moved to the archive location but are not extracted.

## Installation

### Requirements

- Windows
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
pyinstaller --onefile --noconsole --name "FileSort" --icon="assets/icon.ico" --add-data "assets/icon.ico;assets" --collect-all desktop_notifier main.py
```

## Platform Support

### Windows

A ready-to-use Windows executable is provided with each release.

### Linux / macOS

No pre-built executable is currently provided. You can run FileSort from the source code by installing the dependencies and running:

```bash
pip install watchdog pystray pillow desktop-notifier
python main.py
```

PyInstaller builds are platform-specific, so Linux and macOS executables must be built separately on their respective platforms.

## Startup Setup

To start FileSort automatically when the computer starts:

### Windows

1. Keep the FileSort executable in a permanent location. Do not move the executable into the Startup folder.

2. Right-click the executable and select **Create shortcut**.

3. Press **Win + R** and enter:

   `shell:startup`

4. Press **Enter** to open the Windows Startup folder.

5. Move the FileSort shortcut into the Startup folder.

6. Restart Windows to verify that FileSort starts automatically.

To disable automatic startup, simply remove the FileSort shortcut from the Startup folder or disable it from **Settings/Apps/Startup**

### Linux

After building the FileSort executable, you can configure it to start automatically using your desktop environment's Startup Applications settings or a user-level systemd service.

### macOS

After building the FileSort executable, you can add it to System Settings → General → Login Items to start it automatically when you log in.

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
└── assets/
    └── icon.ico
```

## Contribution

Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

## Bug Reports

If you find a bug, please open an issue with:

- A description of the problem
- Steps to reproduce it
- Relevant error messages or screenshots
- Your OS and Python version

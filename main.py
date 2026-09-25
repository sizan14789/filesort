from pathlib import Path
from time import sleep

# local imports
from app_context import BASE
from watchman import watchman
from global_file_handler import handle_file
from system_tray import app

# sweep 1 and watchdog setup
def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

print("Watchman Live!")
watchman.start()
sort_all_once()

# System Tray setup
app.run()
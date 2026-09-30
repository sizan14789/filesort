from pathlib import Path
from time import sleep
import asyncio
import sys

# prevent multiple instances of FileSort running at once, for windows only
if sys.platform == "win32":
    import mutex_file

# local imports
from app_context import BASE, prod
from watchman import watchman
from global_file_handler import handle_file
from system_tray import app
from toaster import notification_coroutine

# sweep 1 and watchdog setup
def sort_all_and_start():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)
    watchman.start()

print("Watchman Live!")
sort_all_and_start()

# Notification and System Tray setup 
asyncio.run(notification_coroutine)

if prod:
    app.run()
else:
    while 1:
        pass
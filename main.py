from pathlib import Path
from time import sleep
import asyncio

# local imports
from app_context import BASE
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

# System Tray setup
asyncio.run(notification_coroutine)
app.run()
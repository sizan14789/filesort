from pathlib import Path
from setup import prod, single_instance, BASE
from watchman import watchman
from main_helper import handle_file
from time import sleep

def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

print("Watchman Live!")
watchman.start()

sort_all_once()

while 1:
    sleep(1)
from pathlib import Path
from setup import prod, single_instance, BASE
from watchman import watchman
from main_helper import handle_file

# sorting previous files before watchdog starts
def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

if prod and single_instance:
    print(f"Sorting {BASE}...")

sort_all_once()

if prod and single_instance:
    print("Done!")
    input()

if single_instance:
    exit()

# watchdog from here
watchman.start()

while True:
    pass
from pathlib import Path
from setup import prod, single_instance, BASE
from watchman import watchman
from main_helper import handle_file
from time import sleep

# defining both processes
def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

# Execution
if not single_instance:
    print("Watchman Live!")
    watchman.start()

if prod and single_instance:
    print(f"Sorting {BASE}...")

sort_all_once()

if prod and single_instance:
    print("Done!")
    input()

if not single_instance:
    while 1:
        sleep(1)
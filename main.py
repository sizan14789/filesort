from pathlib import Path
from setup import prod, single_instance, BASE
from watchman import watchman
from main_helper import handle_file

# defining both process
def sort_all_once():
    for file in BASE.iterdir():
        if file.is_file():
            handle_file(file)

def initiate_watchman(): 
    watchman.start()
    while True:
        pass

# Execution
if not single_instance:
    print("Watchman Live!")
    initiate_watchman()

if prod and single_instance:
    print(f"Sorting {BASE}...")

sort_all_once()

if prod and single_instance:
    print("Done!")
    input()

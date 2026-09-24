from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from setup import BASE
from main_helper import handle_file
from pathlib import Path
from time import sleep

class EventHandler(FileSystemEventHandler):
    def on_created(self, event): 
        handle_file(Path(event.src_path))
        
    def dispatch(self, event):
        if event.is_directory:
            return
        
        print(event.event_type, event.src_path, event.dest_path)
        super().dispatch(event)
        
    def on_moved(self, event):
        file = Path(event.dest_path)

        # to avoid detecting own moves, layer 2
        if file.parent != BASE:
            return
        
        sleep(1) 
        handle_file(file)
        
watchman = Observer()
watchman.schedule(EventHandler(), str(BASE), recursive=False)
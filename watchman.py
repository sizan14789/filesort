from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from setup import BASE
from main_helper import handle_file
from pathlib import Path

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        handle_file(Path(event.src_path))

watchman = Observer()
watchman.schedule(EventHandler(), str(BASE), recursive=False)
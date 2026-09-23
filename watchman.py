from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from setup import BASE
from main_helper import handle_file
from pathlib import Path

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        handle_file(Path(event.src_path))
        
    def dispatch(self, event):
        if event.is_directory:
            return
        super().dispatch(event)
        
    def on_moved(self, event):
        file = Path(event.dest_path)

        if file.parent != BASE:
            return

        handle_file(file)
        
watchman = Observer()
watchman.schedule(EventHandler(), str(BASE), recursive=False)
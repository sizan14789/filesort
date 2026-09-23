from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from setup import BASE

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        print("voala")

watchman = Observer()
watchman.schedule(EventHandler(), str(BASE), recursive=False)
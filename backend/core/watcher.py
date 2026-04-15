import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileSystemHandler(FileSystemEventHandler):
    """Handles file system events and logs them."""
    
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"File created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            logging.info(f"File moved from {event.src_path} to {event.dest_path}")

class FileWatcher:
    """Manages the file system observer and handlers."""
    
    def __init__(self, watch_path="."):
        self.watch_path = watch_path
        self.event_handler = FileSystemHandler()
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.watch_path, recursive=True)
        self.observer.start()
        logging.info(f"Started watching directory: {self.watch_path}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        logging.info("Stopped file watcher.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    watcher = FileWatcher(path)
    watcher.start()
essage)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    watcher = FileWatcher(path)
    watcher.start()

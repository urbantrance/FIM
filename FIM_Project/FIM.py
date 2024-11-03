import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent
from plyer import notification

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.log_event('Modified', event.src_path)

    def on_created(self, event):
        self.log_event('Created', event.src_path)

    def on_deleted(self, event):
        self.log_event('Modified', event.src_path)

    def log_event(self, event_type, file_path):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        file_state = self.get_file_state(file_path)
        with open('change_log.txt', 'a') as f:
            f.write(f'{timestamp} - {event_type}: {file_path} - {file_state}\n')

    def get_file_state(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except (FileNotFoundError, IsADirectoryError):
            return "File not found or is a directory"

def monitor_directory(directory):
    event_handler =ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python_your_script.py <directory_to_monitor>")
        sys.exit(1)
    directory_to_monitor = sys.argv[1]
    monitor_directory(directory_to_monitor)

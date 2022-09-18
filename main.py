import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from update_data import Updater
import config


class Handler(FileSystemEventHandler):
    def on_modified(self, event):

        if (event.src_path == config.PATH_TO_SOURCE_FILE):
            updater = Updater(event.src_path, config.PATH_TO_TARGET_FILES)
            updater.run()


event_handler = Handler()

observer = Observer()

observer.schedule(event_handler, path='./excel/', recursive=False)

observer.start()


if __name__ == "__main__":
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

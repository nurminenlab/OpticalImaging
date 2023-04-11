'''import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()'''

import os
import time

existing_files = set()
baseLine_SC1 = []
SC1 = []
baseLine_SC2 = []
SC2 = []
node = baseLine_SC1

# iterate over the folder to monitor the newly created files
while True:
    files = os.listdir('images')
    tiff_files = [file for file in files if file.endswith('.tiff')]
    
    # save only new file
    new_files = list(set(tiff_files) - existing_files)    
    
    # print only new file
    for tiff_file in new_files:
        print(f"New file created: {tiff_file}")

    # old files update
    existing_files.update(tiff_files)
    
    time.sleep(1)
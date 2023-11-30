import time
import numpy as np
import numpy.typing as npt
import queue
import soundfile as sf
from typing import Iterable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def __init__(self, queue):
        self.queue = queue 

    def on_moved(self, event):
        self.queue.put(event.dest_path)

class FilesystemRecodingsWatcher:
    def __init__(self, path, poll_interval=1):
        self.queue = queue.Queue()
        self.observer = Observer()
        self.observer.schedule(Handler(self.queue), path)
        self.poll_interval = poll_interval


    def watch(self) -> Iterable[
            tuple[npt.NDArray[np.float32], int]
        ]:
        self.observer.start()
        while True:
            start = time.time()

            path = self.queue.get()
            data, sample_rate = sf.read(path)
            
            yield data.astype(np.float32), sample_rate
            
            time.sleep(
                max(0, self.poll_interval - (time.time() - start))
            )

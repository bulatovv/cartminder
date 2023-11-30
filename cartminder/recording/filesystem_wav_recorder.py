import os
import soundfile as sf
import time
import numpy as np
import numpy.typing as npt

from cartminder.recording.sound_capture import AbstractSoundCapturer


class FilesystemWavRecorder:
    def __init__(self, sound_capture: AbstractSoundCapturer, storage_path:  str):
        self.sound_capturer: AbstractSoundCapturer = sound_capture
        self.storage_path: str = storage_path

    def _write(self, capture: npt.NDArray[np.float32]):
        filename = os.path.join(self.storage_path, str(time.time()) + ".wav.locked")


        sf.write(filename, capture, self.sound_capturer.sample_rate, format="wav")
        os.rename(filename, filename.removesuffix(".locked"))

    def record(self):
        for capture in self.sound_capturer.listen():
            self._write(capture)

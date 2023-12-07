import numpy as np
import numpy.typing as npt
import sounddevice as sd

from typing import Iterable

from cartminder.sound_capture.abstract_sound_capturer import AbstractSoundCapturer

class VolumeSoundCapturer(AbstractSoundCapturer):
    def __init__(
        self, 
        sample_rate: int = 16000, 
        block_size: int = 1024, 
        volume_threshold: float = 5,
        max_silence_seconds: int = 4,
    ):
        self.sample_rate: int = sample_rate
        self.block_size: int = block_size
        self.volume_threshold: float = volume_threshold
        self.max_silence_blocks: int = int(max_silence_seconds * sample_rate / block_size)
        self.current_silence_blocks: int = 0
        self.captured: bool = True

        self.captures: list[npt.NDArray[np.float32]] = []
        self.buffer: list[npt.NDArray[np.float32]] = []

        self.stream: sd.InputStream = sd.InputStream(
            samplerate=self.sample_rate,
            blocksize=self.block_size,
            dtype='float32',
            channels=1,
            callback=self._callback
        )


    def _callback(self, indata: npt.NDArray[np.float32], *_):
        volume_norm = np.linalg.norm(indata)
        if np.less(volume_norm, self.volume_threshold):
            self.current_silence_blocks += 1
        else:
            self.current_silence_blocks = 0
            self.captured = False
        
        if self.current_silence_blocks < self.max_silence_blocks and not self.captured:
            self.buffer.append(indata.copy())
        elif not self.captured:
            self.captures.append(np.concatenate(self.buffer))
            self.buffer.clear()
            self.captured = True


    def listen(self) -> Iterable[npt.NDArray[np.float32]]:
        with self.stream: 
            while True:
                if self.captures:
                    yield self.captures.pop(0)

from abc import ABC, abstractmethod
from typing import Iterable
import numpy as np
import numpy.typing as npt

class AbstractSoundCapturer(ABC):
    sample_rate: int
        
    @abstractmethod
    def listen(self) -> Iterable[npt.NDArray[np.float32]]:
        pass

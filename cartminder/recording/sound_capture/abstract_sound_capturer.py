from abc import ABC, abstractmethod
from typing import Iterable
import numpy.typing as npt

class AbstractSoundCapturer(ABC):
    @abstractmethod
    def listen(self) -> Iterable[npt.NDArray]:
        pass

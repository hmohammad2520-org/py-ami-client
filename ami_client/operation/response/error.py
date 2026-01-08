from dataclasses import dataclass
from ._base import Response

@dataclass
class Error(Response):
    def __post_init__(self) -> None:
        self._asterisk_name = 'Error'
        self._label = 'Error'
        super().__post_init__()

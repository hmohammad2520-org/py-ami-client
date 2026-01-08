from dataclasses import dataclass
from ._base import Response

@dataclass
class Success(Response):
    def __post_init__(self) -> None:
        self._asterisk_name = 'Success'
        self._label = 'Success'
        super().__post_init__()

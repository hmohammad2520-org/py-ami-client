from dataclasses import dataclass
from typing import Literal, Optional, Union

from ._base import Action

@dataclass
class Login(Action):
    Username: Optional[str] = None
    Secret: Optional[str] = None
    AuthType: Optional[Literal['plain', 'MD5']] = None
    Key: Optional[str] = None
    Events: Optional[Union[Literal['on', 'off'], list[str]]] = None

    def __post_init__(self):
        self._asterisk_name = 'Login'
        self._label = 'Login'
        super().__post_init__()
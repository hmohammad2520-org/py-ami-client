from typing import Literal, Union

from ._base import Action

class Login(Action):
    def __init__(
            self,*,
            ActionID: int|str,
            Username: str = None,
            Secret: str = None,
            AuthType: Literal['plain', 'MD5'] = None,
            Key: str = None,
            Events: Union[Literal['on', 'off'], list[str]] = None,
    ) -> None:

        self._asterisk_name = 'Login'
        self._label = 'Login'

        self.username = Username
        self.secret = Secret
        self.auth_type = AuthType
        self.key = Key
        self.events = Events

        kwargs = {
            'ActionID': ActionID,
            'Username': Username,
            'Secret': Secret,
            'AuthType': AuthType,
            'Key': Key,
            'Events': Events,
        }
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(**filtered_kwargs)

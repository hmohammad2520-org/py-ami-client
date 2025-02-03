from typing import Literal, Union

from ..response.success import Success

from ._base import Action

class Login(Action):
    def __init__(
            self,*,
            ActionID: int|str = None,
            Username: str = None,
            Secret: str = None,
            AuthType: Literal['plain', 'MD5'] = None,
            Key: str = None,
            Events: Union[Literal['on', 'off'], list[str]] = None,
            **additional_kwargs
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
        kwargs.update(additional_kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(Action=self._asterisk_name, **filtered_kwargs)

    def send(self, client, raise_on_no_response=True) -> Success:
        self.response: Success
        return super().send(client, raise_on_no_response)

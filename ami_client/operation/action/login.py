from typing import Literal, Optional, Union

from ami_client.operation.response import Response

from ._base import Action

class Login(Action):
    def __init__(
            self,*,
            ActionID: Optional[int] = None,
            Username: Optional[str] = None,
            Secret: Optional[str] = None,
            AuthType: Optional[Literal['plain', 'MD5']] = None,
            Key: Optional[str] = None,
            Events: Optional[Union[Literal['on', 'off'], list[str]]] = None,
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

    def send(self, client, raise_on_no_response: bool = True) -> Response | None:
        client.connect()
        return super().send(client, raise_on_no_response)
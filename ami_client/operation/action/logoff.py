from typing import Optional
from ami_client.operation.response import Response
from ._base import Action

class Logoff(Action):
    def __init__(
            self,*,
            ActionID: Optional[int] = None,
            **additional_kwargs
    ) -> None:

        self._asterisk_name = 'Logoff'
        self._label = 'Logoff'

        kwargs = {
            'ActionID': ActionID,
        }
        kwargs.update(additional_kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(Action=self._asterisk_name, **filtered_kwargs)

    def send(self, client, raise_on_no_response: bool = True) -> Response | None:
        response = super().send(client, raise_on_no_response)
        client.disconnect()
        return response
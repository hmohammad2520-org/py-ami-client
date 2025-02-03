from typing import Literal, Union

from ..response.success import Success

from ._base import Action

class Ping(Action):
    def __init__(
            self,*,
            ActionID: int|str = None,
            **additional_kwargs,
    ) -> None:

        self._asterisk_name = 'Ping'
        self._label = 'Ping'

        kwargs = {
            'ActionID': ActionID,
        }
        kwargs.update(additional_kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(Action=self._asterisk_name, **filtered_kwargs)

    def send(self, client, raise_on_no_response=True) -> Success:
        self.response: Success
        return super().send(client, raise_on_no_response)

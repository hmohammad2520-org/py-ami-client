from ._base import Action

class Logoff(Action):
    def __init__(
            self,*,
            ActionID: int|str = None,
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

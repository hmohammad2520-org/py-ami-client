from ._base import Response

class Success(Response):
    def __init__(
            self,*,
            Response: str,
            ActionID: int|str = None,
            Message: str = None,
    ) -> None:

        self.asterisk_name = 'Login'
        self.label = 'Login'

        self.message = Message

        kwargs = {
            'Response': Response,
            'ActionID': ActionID,
            #'Message': Message,
        }
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(**filtered_kwargs)

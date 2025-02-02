from ...operation.response import Response
from ...operation._base import Operation

class Action(Operation):
    def __init__(self) -> None:
        self.sent: bool = None
        self.response: Response = None
        super().__init__()

    def send(self, client, handler) -> Response:
        ...
    
    def __bool__(self) -> bool:
        return self.sent
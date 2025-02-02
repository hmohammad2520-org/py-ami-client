from ...operation.response import Response
from ...operation._base import Operation

class Action(Operation):
    def __init__(self, Action: str ,ActionID: int, **kwargs) -> None:
        self.sent: bool = None
        self.response: Response = None
        self.action = Action
        self.action_id: int = int(ActionID)
        super().__init__(Action=Action, ActionID=ActionID, **kwargs)

    def send(self, client, handler) -> Response:
        # Implement your send logic here
        pass

    def __bool__(self) -> bool:
        return self.sent
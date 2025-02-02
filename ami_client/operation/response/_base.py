from ...operation._base import Operation

class Response(Operation):
    def __init__(self, Response: str, ActionID: int, **kwargs):
        self.response = Response
        self.action_id = int(ActionID)
        super().__init__(Response=Response, ActionID=ActionID, **kwargs)
from ...operation._base import Operation

class Response(Operation):
    def __init__(self, Response: str):
        self.response = Response
        super().__init__(Response=Response)
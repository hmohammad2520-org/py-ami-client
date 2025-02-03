import time, random

from ...operation.response import Response
from ...operation._base import Operation

class Action(Operation):
    def __init__(self, Action: str ,ActionID: int = None, **kwargs) -> None:
        self.sent: bool = None
        self.response: Response = None
        self.action = Action
        self.action_id: int = int(ActionID) if ActionID else random.randint(0, 1_000_000)
        super().__init__(Action=Action, ActionID=self.action_id, **kwargs)

    def send(self, client: 'AMIClient', raise_on_no_response: bool = True) -> Response|None: # type: ignore
        action_string = self.convert_to_raw_content(self._dict)
        client.socket.sendall(action_string.encode())
        self.sent = True

        start = time.time()
        while (time.time() - start) < client.timeout:
            if not client.connected:
                break

            response = client.registery.get_response(action_id=self.action_id)
            if response:
                self.response = response
                client.registery.remove_response(response)
                return response

            #for prevent tight locking
            time.sleep(0.05)

        else:
            if not raise_on_no_response:
                self.response = None
                raise TimeoutError(
                    f'Timeout while getting response. action: {self.action} - action id: {self.action_id}'
                    )

            else:
                self.response = None
                return None

    def __bool__(self) -> bool:
        return self.sent
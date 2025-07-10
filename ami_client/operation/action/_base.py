import time, random
from typing import Optional

from ...operation.response import Response
from ...operation._base import Operation

class Action(Operation):
    from ami_client import AMIClient

    def __init__(self, Action: str ,ActionID: Optional[int] = None, **kwargs) -> None:
        self.sent: bool = False
        self.server_response: Response | None = None
        self.action = Action
        self.action_id: int = int(ActionID) if ActionID else random.randint(0, 1_000_000_000)
        super().__init__(Action=Action, ActionID=self.action_id, **kwargs)

    def send(self, client: AMIClient, raise_on_no_response: bool = True) -> Response | None:
        action_string = self.convert_to_raw_content(self._dict)
        client.socket.sendall(action_string.encode())
        self.sent = True

        start = time.time()
        while (time.time() - start) < client.timeout:
            if not client.connected:
                break

            response = client.registry.get_response(action_id=self.action_id)
            if response:
                self.server_response = response
                client.registry.remove_response(response)
                return response

            time.sleep(0.05)  # prevent tight locking

        else:
            if not raise_on_no_response:
                self.server_response = None
                raise TimeoutError(
                    f'Timeout while getting response. action: {self.action} - action id: {self.action_id}'
                )

            else:
                self.server_response = None
                return None

    def __bool__(self) -> bool:
        return self.sent
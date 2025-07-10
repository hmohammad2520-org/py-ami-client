import time
from typing import Any, Dict, List

from ._exeptions import AMIExceptions
from .operation import Action, Event, Response, UnkhownOP


class Channel:
    def __init__(self, channel_id: str, **kwargs):
        self.channel_id = channel_id
        self.timestamp: float = time.time()
        self.dict: Dict[str, Any] = kwargs

        self.actions: List[Action | UnkhownOP] = []
        self.events: List[Event | UnkhownOP] = []
        self.responses: List[Response | UnkhownOP] = []

    def add_operation(self, operation) -> None:
        if isinstance(operation, Action) or hasattr(operation, 'action'):
            self.actions.append(operation)

        elif isinstance(operation, Event) or hasattr(operation, 'event'):
            self.events.append(operation)

        elif isinstance(operation, Response) or hasattr(operation, 'response'):
            self.responses.append(operation)

        else:
            raise AMIExceptions.ClntSide.OperationError(
                'operation must be an instance of Operation subclasses'
                )

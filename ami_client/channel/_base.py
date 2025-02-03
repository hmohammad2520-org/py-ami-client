import time
from typing import Any, Dict
from ..operation import Action, Event, Response, Unkhown

class Channel:
    def __init__(self, channel_id: str, **kwargs):
        self.channel_id = channel_id
        self.timestamp: float = time.time()
        self.dict: Dict[str, Any] = kwargs

        self.actions: list[Action] = []
        self.events: list[Event] = []
        self.responses: list[Response] = []

    def add_operation(self, operation: Action|Event|Response|Unkhown) -> None:
        ...

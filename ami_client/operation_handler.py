from typing import Callable
from .exeptions import AMIException

class OperationHandler:
    def __init__(self):
        self._responses: dict = {}
        self._event_function_map: dict[str, list[Callable]] = {}
        self._events_functions: list[Callable] = []

    def handel_event(self, event: dict) -> None:
        functions = self._event_function_map.get(event.get('Event'), list())
        functions += self._events_functions

        for function in functions:
            function(event)

    def add_event_function(self, function: Callable, events: str|list|None = None) -> None:
        if events is None:
            self._events_functions.append(function)
            return

        if isinstance(events, str):
            events = [events,]
        
        for event in events:
            if event not in self._event_function_map.keys():
                self._event_function_map[event] = []
            
            self._event_function_map[event].append(function)

    def remove_event_function(self, function: Callable, events: str|list|None = None) -> None:
        if events is None:
            self._events_functions.remove(function)
            return
        
        if isinstance(events, str):
            events = [events,]
        
        for event in events:
            self._event_function_map[event].remove(function)


    def handel_response(self, response: dict) -> None:
        action_id = int(response.get('ActionID'))
        if not action_id:
            raise TypeError('response is not in currect format')
        
        if action_id in self._responses.keys():
            raise AMIException('Duplication in Action ID, please check the action number.')

        self._responses[action_id] = response


    def get_response(self, action_id: int) -> dict | None:
        return self._responses.get(action_id)


    def remove_response(self, action_id: int) -> None:
        self._responses.pop(action_id)

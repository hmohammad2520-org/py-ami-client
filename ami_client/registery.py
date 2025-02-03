from typing import Dict
from .operation import Operation, Action, Event, Response, Unkhown
from .operation import action_map, event_map, response_map
from .channel import Channel

class Registery:
    def __init__(self):
        self.action_id = 0
        self.actions: Dict[int, Action] = {}

        self.event_id = 0
        self.events: Dict[int, Event] = {}

        self.response_id = 0
        self.responses: Dict[int, Response] = {}

        self.channels: Dict[str, Channel] = {}

        self.white_list: list[str] = []
        self.black_list: list[str] = []

    def register_operation(self, raw_operation) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if operation_dict:
            if 'Action' in operation_dict.keys():
                operation_class = action_map.get(operation_dict['Action'])

            elif 'Event' in operation_dict.keys():
                operation_class = event_map.get(operation_dict['Event'])

            elif 'Response' in operation_dict.keys():
                operation_class = response_map.get(operation_dict['Response'])

            else:
                raise ValueError('Parsed unkhown data from server')

            if not operation_class:
                operation_class = Unkhown

            operation = operation_class(**operation_dict)
            self.init_channel(operation)
            self.add_operation(operation)

        else:
            raise ValueError('Unable to parse the operation to dict -> got None')


    def add_operation(self, operation: Action|Event|Response|Unkhown) -> None:
        print(operation._dict)
        print()

        if hasattr(operation, 'action'):
            self.action_id += 1
            operation._list_id = self.action_id
            self.actions[self.action_id] = operation

        elif hasattr(operation, 'event'):
            self.event_id += 1
            operation._list_id = self.event_id
            self.events[self.event_id] = operation

        elif hasattr(operation, 'response'):
            self.response_id += 1
            operation._list_id = self.response_id
            self.responses[self.response_id] = operation

        else:
            raise ValueError(f'operation must be an instance of Operation subclasses')


    def get_response(self,*, response_id: int=None, action_id: int=None) -> Response | None:
        if response_id:
            return self.responses.get(response_id)

        elif action_id:
            for response in self.responses.values():
                if response.action_id == action_id:
                    return response

        else:
            raise ValueError('Provide response_id or action_id')

    def remove_response(self, response: Response):
        if response._list_id in self.responses:
            self.responses.pop(response._list_id)
    
    def init_channel(self, operation: Operation) -> None:
        if hasattr(operation, 'channel'):
            ...

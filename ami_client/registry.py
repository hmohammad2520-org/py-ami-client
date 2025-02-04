from typing import Dict, Set, Type

from .exeptions import AMIException

from .channel import Channel
from .operation import Operation, Action, Event, Response, Unkhown
from .operation import action_map, event_map, response_map

class Registry:
    def __init__(self) -> None:
        self.action_id: int = 0
        self.actions: Dict[int, Action] = {}

        self.event_id: int = 0
        self.events: Dict[int, Event] = {}

        self.response_id: int = 0
        self.responses: Dict[int, Response] = {}

        self.channels: Dict[str, Channel] = {}

        self.whitelist: Set[Type] = set()
        self.blacklist: Set[Type] = set()


    def register_operation(self, raw_operation: str) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if operation_dict:
            if 'Action' in operation_dict.keys():
                operation_class = action_map.get(operation_dict['Action'])

            elif 'Event' in operation_dict.keys():
                operation_class = event_map.get(operation_dict['Event'])

            elif 'Response' in operation_dict.keys():
                operation_class = response_map.get(operation_dict['Response'])

            else:
                raise AMIException.ClntSide.UnknownOperation(
                    'Parsed unkhown data from server'
                    )

            if not operation_class:
                operation_class = Unkhown

            if self.whitelist:
                for cls in self.whitelist:
                    if not issubclass(operation_class, cls) or operation_class == cls: return

            if self.blacklist:
                for cls in self.blacklist:
                    if issubclass(operation_class, cls) or operation_class == cls: return

            operation = operation_class(**operation_dict)
            self.init_channel(operation)
            self.add_operation(operation)

        else:
            raise AMIException.ClntSide.InvalidOperation(
                'Unable to parse the operation to dict -> got None'
                )


    def add_operation(self, operation: Action|Event|Response|Unkhown) -> None:
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
            raise AMIException.ClntSide.OperationError(
                'operation must be an instance of Operation subclasses'
                )


    def get_response(self,*, response_id: int=None, action_id: int=None) -> Response|None:
        response = None

        if response_id:
            response = self.responses.get(response_id)

        elif action_id:
            for res in self.responses.values():
                if res.action_id == action_id:
                    response = res
                    break
        else:
            raise AMIException.ClntSide.ResponseError('Provide response_id or action_id')

        return response

    def remove_response(self, response: Response) -> None:
        if response._list_id in self.responses:
            self.responses.pop(response._list_id)
    
    def init_channel(self, operation: Operation) -> None:
        if hasattr(operation, 'channel'):
            ...

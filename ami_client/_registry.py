from typing import Set, Type, Deque
from collections import deque
from .operation import Operation, Action, Event, Response, UnkhownOP
from .operation import action_map, event_map, response_map
from ._channel import Channel
from ._exeptions import AMIExceptions


class Registry:
    def __init__(self) -> None:
        self.actions: Deque[Action] = deque(maxlen=1000)
        self.events: Deque[Event] = deque(maxlen=1000)
        self.responses: Deque[Response] = deque(maxlen=1000)
        self.channels: Deque[Channel] = deque(maxlen=1000)

        self.whitelist: Set[Type[Operation]] = set()
        self.blacklist: Set[Type[Operation]] = set()

    def _register_new_operation(self, raw_operation: str) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if operation_dict:
            if 'Action' in operation_dict.keys():
                operation_class = action_map.get(operation_dict['Action'])

            elif 'Event' in operation_dict.keys():
                operation_class = event_map.get(operation_dict['Event'])

            elif 'Response' in operation_dict.keys():
                operation_class = response_map.get(operation_dict['Response'])

            else:
                raise AMIExceptions.ClntSide.UnknownOperation(
                    'Parsed unkhown data from server'
                )

            if operation_class is None:
                operation_class = UnkhownOP

            if self.whitelist:
                for cls in self.whitelist:
                    if not issubclass(operation_class, cls) or operation_class == cls: return

            if self.blacklist:
                for cls in self.blacklist:
                    if issubclass(operation_class, cls) or operation_class == cls: return

            operation = operation_class(**operation_dict)
            #self.init_channel(operation)  # Not Implemented Yet
            self._add_operation(operation)

        else:
            raise AMIExceptions.ClntSide.InvalidOperation(
                'Unable to parse the operation to dict -> got None'
            )


    def _add_operation(self, operation) -> None:
        if isinstance(operation, Action) and hasattr(operation, 'action'):
            self.actions.append(operation)

        elif isinstance(operation, Event) and hasattr(operation, 'event'):
            self.events.append(operation)

        elif isinstance(operation, Response) and hasattr(operation, 'response'):
            self.responses.append(operation)

        else:
            raise AMIExceptions.ClntSide.OperationError(
                'operation must be an instance of Operation subclasses'
                )


    def get_response(self, action_id: int) -> Response|None:
        server_response = None
        for response in self.responses:
            if int(response.action_id) == int(action_id):
                server_response = response
                break

        return server_response

    def init_channel(self, operation: Operation) -> None:
        raise NotImplementedError

from .operation import Operation, Action, Event, Response
from .operation import action_map, event_map, response_map

class OperationHandler:
    def __init__(self, name: str):
        self.name = name

        self.actions = []
        self.events = []
        self.responses = []

    def handel_operation(self, raw_operation) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if operation_dict:
            if 'Action' in operation_dict.keys():
                action_class = action_map.get(operation_dict['Action'])
                if not action_class:
                    raise ValueError(f'Unkhown Operation name from server: <Action {operation_dict['Response']}')

                action = action_class(**operation_dict)
                self.handel_action(action)

            elif 'Event' in operation_dict.keys():
                event_class = event_map.get(operation_dict['Event'])
                if not event_class:
                    raise ValueError(f'Unkhown Operation name from server: <Event {operation_dict['Response']}')

                event = event_class(**operation_dict)
                self.handel_event(event)

            elif 'Response' in operation_dict.keys():
                response_class = response_map.get(operation_dict['Response'])
                if not response_class:
                    raise ValueError(f'Unkhown Operation name from server: <Response {operation_dict['Response']}>')

                response = response_class(**operation_dict)
                self.handel_response(response)

            else:
                raise ValueError('Parsed unkhown data from server')

        else:
            raise ValueError('Unable to parse the operation to dict -> got None')
    
    def handel_action(self, action: Action) -> None:
        self.actions.append(action)
    
    def handel_event(self, event: Event) -> None:
        self.events.append(event)
    
    def handel_response(self, response: Response) -> None:
        self.responses.append(response)
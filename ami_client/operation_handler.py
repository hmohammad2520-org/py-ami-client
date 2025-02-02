from typing import Dict
from .operation import Operation, Action, Event, Response, Unkhown
from .operation import action_map, event_map, response_map


class OperationHandler:
    def __init__(self):
        self.action_id = 0
        self.event_id = 0
        self.response_id = 0

        self.actions: Dict[int, Action] = {}
        self.events: Dict[int, Event] = {}
        self.responses: Dict[int, Response] = {}

    def handel_operation(self, raw_operation) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if operation_dict:
            if 'Action' in operation_dict.keys():
                action_class = action_map.get(operation_dict['Action'])
                if not action_class:
                    action_class = Unkhown

                action = action_class(**operation_dict)
                self.add_action(action)

            elif 'Event' in operation_dict.keys():
                event_class = event_map.get(operation_dict['Event'])
                if not event_class:
                    event_class = Unkhown

                event = event_class(**operation_dict)
                self.add_event(event)

            elif 'Response' in operation_dict.keys():
                response_class = response_map.get(operation_dict['Response'])
                if not response_class:
                    response_class = Unkhown

                response = response_class(**operation_dict)
                self.add_response(response)

            else:
                raise ValueError('Parsed unkhown data from server')

        else:
            raise ValueError('Unable to parse the operation to dict -> got None')


    def add_action(self, action: Action) -> None:
        self.action_id += 1
        action.list_id = self.action_id
        self.actions[self.action_id] = action

    def add_event(self, event: Event) -> None:
        self.event_id += 1
        event.list_id = self.event_id
        self.events[self.event_id] = event

    def add_response(self, response: Response) -> None:
        self.response_id += 1
        response.list_id = self.response_id
        self.responses[self.response_id] = response


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
        if response.list_id in self.responses:
            self.responses.pop(response.list_id)
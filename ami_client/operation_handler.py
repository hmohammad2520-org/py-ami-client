from typing import Callable
from operation import Operation

class OperationHandler:
    def __init__(self, name: str):
        self.name = name

        self.actions = []
        self.events = []
        self.responses = []

    def create_operation(raw_operation) -> None:
        operation_dict = Operation.parse_raw_content(raw_operation)
        if 'Action' in operation_dict.keys():
            ...
        
        elif 'Event' in operation_dict.keys():
            ...
        
        elif 'Response' in operation_dict.keys():
            ...
        
        else:
            ...

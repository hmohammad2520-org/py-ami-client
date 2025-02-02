from typing import Any, Dict, Type
import time

ASTERISK_BANNER: str = 'Asterisk Call Manager'

class Operation:
    def __init__(self, **kwargs):
        self.list_id: int = None
        self.raw: str = ''
        self.dict: Dict[str, Any] = {}
        self.asterisk_name: str = ''
        self.label: str = ''
        self.timestamp: float = time.time()

        self.dict.update(kwargs)
        self.raw = self.convert_to_raw_content(self.dict)

    @staticmethod
    def parse_raw_content(raw: str) -> Dict[str, Any]:
        lines = raw.strip().split('\r\n')
        operation_dict: Dict[str, Any] = {}
        for line in lines:
            if ASTERISK_BANNER in line: continue

            key, value = line.split(':', 1)
            operation_dict[key.lstrip()] = value.lstrip()

        return operation_dict

    @staticmethod
    def convert_to_raw_content(operation_dict: Dict[str, Any]) -> str:
        raw_operation: str = ''
        for key, value in operation_dict.items():
            raw_operation += f'{key.replace('_', '-')}: {value}\r\n'

        raw_operation += '\r\n'
        return raw_operation

    def __str__(self) -> str:
        return f'<Operation: {self.asterisk_name}>'

    def __repr__(self) -> str:
        return f'<Operation: {self.asterisk_name}>'

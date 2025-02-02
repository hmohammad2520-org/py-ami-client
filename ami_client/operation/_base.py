from datetime import datetime

class Operation:
    _raw: str
    _dict: dict
    _value_type_map: dict
    timestamp: datetime

    @staticmethod
    def parse_raw_content(raw:str) -> dict:
        lines = raw.strip().split('\r\n')
        operation_dict = {}
        for line in lines:
            if 'Asterisk Call Manager' in line: continue
            key, value = line.split(':', 1)
            operation_dict[key.lstrip()] = value.lstrip().split(',') if ',' in value else value.lstrip()

        return operation_dict


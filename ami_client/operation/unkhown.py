from ._base import Operation

class Unkhown(Operation):
    def __init__(self, **kwargs):
        
        self.asterisk_name: str = 'Unkhown'
        self.label: str = 'Unkhown'

        if 'Action' in kwargs.keys():
            self.action = kwargs.get('Action')
            self.action_id = int(kwargs.get('ActionID'))

        elif 'Event' in kwargs.keys():
            self.event = kwargs.get('Event')

        elif 'Response' in kwargs.keys():
            self.response = kwargs.get('Response')
            self.action_id = int(kwargs.get('ActionID'))

        super().__init__(**kwargs)

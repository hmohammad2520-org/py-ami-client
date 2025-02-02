from ._base import Operation

class Unkhown(Operation):
    def __init__(self, **kwargs):
        
        self.asterisk_name: str = 'Unkhown'
        self.label: str = 'Unkhown'

        super().__init__(**kwargs)

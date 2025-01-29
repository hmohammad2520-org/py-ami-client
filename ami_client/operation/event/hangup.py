from ._base import Event

class Hangup(Event):
    def __init__(
            self,
            channel:str = None,
            channel_state:str = None,
            channel_state_desc:str = None,
            callerid_num:str = None,
            callerid_name:str = None,
            connected_line_num:str = None,
            connected_line_name:str = None,
            language:str = None,
            account_code:str = None,
            context:str = None,
            exten:str = None,
            priority:str = None,
            uniqueid:str = None,
            linkedid:str = None,
            cause:str = None,
            cause_txt:str = None,
            ) -> None:

        self.channel = channel
        self.channel_state = channel_state
        self.channel_state_desc = channel_state_desc
        self.callerid_num = callerid_num
        self.callerid_name = callerid_name
        self.connected_line_num = connected_line_num
        self.connected_line_name = connected_line_name
        self.language = language
        self.account_code = account_code
        self.context = context
        self.exten = exten
        self.priority = priority
        self.uniqueid = uniqueid
        self.linkedid = linkedid
        self.cause = cause
        self.cause_txt = cause_txt

        self._asterisk_name = 'Hangup'
        self._label = 'Hangup'
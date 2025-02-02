from ._base import Event

class Hangup(Event):
    def __init__(
            self, *,
            Event: str = None,
            Channel: str = None,
            ChannelState: str = None,
            ChannelStateDesc: str = None,
            CallerIDNum: str = None,
            CallerIDName: str = None,
            ConnectedLineNum: str = None,
            ConnectedLineName: str = None,
            Language: str = None,
            AccountCode: str = None,
            Context: str = None,
            Exten: str = None,
            Priority: str = None,
            Uniqueid: str = None,
            Linkedid: str = None,
            Cause: str = None,
            Cause_txt: str = None,
    ) -> None:
        self._asterisk_name = 'Hangup'
        self._label = 'Hangup'

        self.event = Event
        self.channel = Channel
        self.channel_state = ChannelState
        self.channel_state_desc = ChannelStateDesc
        self.callerid_num = CallerIDNum
        self.callerid_name = CallerIDName
        self.connected_line_num = ConnectedLineNum
        self.connected_line_name = ConnectedLineName
        self.language = Language
        self.account_code = AccountCode
        self.context = Context
        self.exten = Exten
        self.priority = Priority
        self.uniqueid = Uniqueid
        self.linkedid = Linkedid
        self.cause = Cause
        self.cause_txt = Cause_txt

        kwargs = {
            'Event': Event,
            'Channel': Channel,
            'ChannelState': ChannelState,
            'ChannelStateDesc': ChannelStateDesc,
            'CallerIDNum': CallerIDNum,
            'CallerIDName': CallerIDName,
            'ConnectedLineNum': ConnectedLineNum,
            'ConnectedLineName': ConnectedLineName,
            'Language': Language,
            'AccountCode': AccountCode,
            'Context': Context,
            'Exten': Exten,
            'Priority': Priority,
            'Uniqueid': Uniqueid,
            'Linkedid': Linkedid,
            'Cause': Cause,
            'Cause_txt': Cause_txt,
        }
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(**filtered_kwargs)
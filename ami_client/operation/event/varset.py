from ._base import Event

class VarSet(Event):
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
            Variable: str = None,
            Value: str = None,
            **additional_kwargs
    ) -> None:

        self._asterisk_name = 'VarSet'
        self._label = 'Variable Set'

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
        self.Variable = Variable
        self.Value = Value

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
            'Variable': Variable,
            'Value': Value,
        }
        kwargs.update(additional_kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(**filtered_kwargs)
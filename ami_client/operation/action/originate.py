from ._base import Action

class Originate(Action):
    def __init__(
            self,*,
            ActionID: int|str = None,
            Channel: str = None,
            Exten: str = None,
            Context: str = None,
            Priority: str = None,
            Application: str = None,
            Data: str = None,
            Timeout: str = None,
            CallerID: str = None,
            Variable: str = None,
            Account: str = None,
            EarlyMedia: str = None,
            Async: str = None,
            Codecs: str = None,
            ChannelId: str = None,
            OtherChannelId: str = None,
            PreDialGoSub: str = None,
            **additional_kwargs
    ) -> None:

        self._asterisk_name = 'Originate'
        self._label = 'Originate'

        self.channel = Channel
        self.exten = Exten
        self.context = Context
        self.priority = Priority
        self.application = Application
        self.data = Data
        self.timeout = Timeout
        self.caller_id = CallerID
        self.variable = Variable
        self.account = Account
        self.early_media = EarlyMedia
        self.Async = Async
        self.codecs = Codecs
        self.channel_id = ChannelId
        self.other_channel_id = OtherChannelId
        self.pre_dial_go_sub = PreDialGoSub


        kwargs = {
            'ActionID': ActionID,
            'Channel': Channel,
            'Exten': Exten,
            'Context': Context,
            'Priority': Priority,
            'Application': Application,
            'Data': Data,
            'Timeout': Timeout,
            'CallerID': CallerID,
            'Variable': Variable,
            'Account': Account,
            'EarlyMedia': EarlyMedia,
            'Async': Async,
            'Codecs': Codecs,
            'ChannelId': ChannelId,
            'OtherChannelId': OtherChannelId,
            'PreDialGoSub': PreDialGoSub,
        }
        kwargs.update(additional_kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        super().__init__(Action=self._asterisk_name, **filtered_kwargs)

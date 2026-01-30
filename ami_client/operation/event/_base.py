from dataclasses import dataclass, field
from typing import Optional, Callable, Dict, List, Type, TypeAlias, Literal
from collections import defaultdict

from ...operation._base import Operation

ChannelStateDescType: TypeAlias = Literal[
    'Down', 'Rsrvd', 'OffHook', 'Dialing', 
    'Ringing', 'Up', 'Busy', 'Dialing Offhook',
    'Pre-ring', 'Unknown', 'Ring',
]

@dataclass
class Event(Operation):
    Event: Optional[str] = None
    Privilege: Optional[str] = None

    def __post_init__(self):
        self.Event = self._asterisk_name


@dataclass
class ChannelEventMixin:
    Channel: Optional[str] = None
    ChannelState: Optional[str] = None
    ChannelStateDesc: Optional[ChannelStateDescType] = None
    CallerIDNum: Optional[str] = None
    CallerIDName: Optional[str] = None
    ConnectedLineNum: Optional[str] = None
    ConnectedLineName: Optional[str] = None
    Language: Optional[str] = None
    AccountCode: Optional[str] = None
    Context: Optional[str] = None
    Exten: Optional[str] = None
    Priority: Optional[str] = None
    Uniqueid: Optional[str] = None
    Linkedid: Optional[str] = None

@dataclass
class DestChannelEventMixin:
    DestChannel: Optional[str] = None
    DestChannelState: Optional[str] = None
    DestChannelStateDesc: Optional[ChannelStateDescType] = None
    DestCallerIDNum: Optional[str] = None
    DestCallerIDName: Optional[str] = None
    DestConnectedLineNum: Optional[str] = None
    DestConnectedLineName: Optional[str] = None
    DestLanguage: Optional[str] = None
    DestAccountCode: Optional[str] = None
    DestContext: Optional[str] = None
    DestExten: Optional[str] = None
    DestPriority: Optional[str] = None
    DestUniqueid: Optional[str] = None
    DestLinkedid: Optional[str] = None


class EventDispatcher:
    def __init__(self):
        self.handlers: Dict[Type[Event], List[Callable]] = defaultdict(list)

    def register(
            self,
            key: Type[Event],
            handler: Callable,
        ) -> None:
        self.handlers[key].append(handler)

    def dispatch(self, event) -> None:
        # By class (Event, Hangup, etc.)
        for cls, handlers in self.handlers.items():
            if isinstance(event, cls):
                for handler in handlers:
                    handler(event)

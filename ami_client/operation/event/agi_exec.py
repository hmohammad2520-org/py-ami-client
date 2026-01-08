from dataclasses import dataclass
from typing import Optional

from ._base import Event, ChannelEventMixin

@dataclass
class AGIExecEnd(Event, ChannelEventMixin):
    Command: Optional[str] = None
    CommandId: Optional[str] = None
    ResultCode: Optional[str] = None
    Result: Optional[str] = None

    def __post_init__(self):
        self._asterisk_name = 'AGIExecEnd'
        self._label = 'AGI Exec End'
        return super().__post_init__()


@dataclass
class AGIExecStart(Event, ChannelEventMixin):
    Command: Optional[str] = None
    CommandId: Optional[str] = None

    def __post_init__(self):
        self._asterisk_name = 'AGIExecStart'
        self._label = 'AGI Exec Start'
        return super().__post_init__()

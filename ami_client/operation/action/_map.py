from ._base import Action
from typing import Type

ACTION = Type[Action]

action_map: dict[str, ACTION] = {}
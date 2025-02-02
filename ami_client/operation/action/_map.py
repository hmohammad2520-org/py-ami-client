from typing import Type

from ._base import Action
from .login import Login

ACTION = Type[Action]

action_map: dict[str, ACTION] = {
    'Login': Login,
}
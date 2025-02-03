from typing import Type

from ._base import Action
from .login import Login

action_map: dict[str, Type[Action]] = {
    'Login': Login,
}
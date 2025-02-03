from typing import Type

from ._base import Response
from .success import Success

response_map: dict[str, Type[Response]] = {
    'Success': Success,
}
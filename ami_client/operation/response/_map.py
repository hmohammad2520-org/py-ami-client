from typing import Type

from ._base import Response
from .success import Success

RESPONSE = Type[Response]

response_map: dict[str, RESPONSE] = {
    'Success': Success,
}
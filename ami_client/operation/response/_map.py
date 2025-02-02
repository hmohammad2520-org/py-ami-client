from ._base import Response
from typing import Type


RESPONSE = Type[Response]

response_map: dict[str, RESPONSE] = {}
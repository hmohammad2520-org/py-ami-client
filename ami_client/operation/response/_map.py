from typing import Type

from ._base import Response


RESPONSE = Type[Response]

response_map: dict[str, RESPONSE] = {}
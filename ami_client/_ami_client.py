import socket, threading
from typing import List, Literal, Optional, Self, Type, Union, cast

from ._exeptions import AMIExceptions

EXCEPTED_OS_ERROR  =  'An operation was attempted on something that is not a socket'

class AMIClient:
    from .operation import Operation, Response

    def __init__(
            self,
            host: str = '127.0.0.1',
            port: int = 5038,
            Username: Optional[str] = None,
            Secret: Optional[str] = None,
            AuthType: Optional[Literal['plain', 'MD5']] = None,
            Key: Optional[str] = None,
            Events: Optional[Union[Literal['on', 'off'], list[str]]] = None,
            timeout: int = 10,
            socket_buffer: int = 2048,
        ) -> None:

        self._host = host
        self._port = port
        self._username = Username
        self._secret = Secret
        self._auth_type = AuthType
        self._key = Key
        self._events = Events
        self._timeout = timeout
        self._socket_buffer = socket_buffer

        self.connected = False
        self.authenticated = False

        from ._registry import Registry
        self.registry = Registry()


    def connect(self) -> None:
        if not self.connected:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self._timeout)
            self.listen_thread = threading.Thread(target=self.listen_loop, daemon=True)

            self.connected = True
            self.socket.connect((self._host, self._port))
            self.listen_thread.start()

    def disconnect(self) -> None:
        if self.authenticated:
            self.logout()

        if self.connected:
            self.connected = False
            if not threading.current_thread() == self.listen_thread:
                self.listen_thread.join()

            self.socket.close()

    def listen_loop(self) -> None:
        buffer = b''

        while self.connected:
            try: data = self.socket.recv(self._socket_buffer)
            ## This error excepted if no event triggers in server for `self._timeout` amount of time.
            except TimeoutError: continue
            except OSError as e:
                ## This error message is excepted sometimes and this line prevents random crashes
                if EXCEPTED_OS_ERROR in str(e): continue
                else:
                    self.disconnect()
                    raise e

            try:
                buffer += data
                while b'\r\n\r\n' in buffer:
                    raw_operation, buffer = buffer.split(b'\r\n\r\n', 1)
                    self.registry._register_new_operation(raw_operation.decode())

            ## Ignore Operation Errors
            ## TODO: This is a temporary solution. This will be fixed in logging integration.
            except AMIExceptions.ClientError.OperationError: continue
            except Exception as e:
                self.disconnect()
                raise e


    def login(self) -> Response:
        from .operation import Response
        from .operation.action import Login
        from .operation.response import Success

        response = Login(
            Username = self._username,
            Secret = self._secret,
            AuthType = cast(Optional[Literal['plain', 'MD5']], self._auth_type),
            Key = self._key,
            Events = cast(Optional[Union[Literal['on', 'off'], list[str]]], self._events),
        ).send(self)

        self.authenticated = True if isinstance(response, Success) else False
        return cast(Response, response)

    def logout(self) -> Response | None:
        from .operation.action import Logoff
        self.authenticated = False
        return Logoff().send(self)


    def add_whitelist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.whitelist.add(item)

    def add_blacklist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.blacklist.add(item)


    def remove_whitelist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.whitelist.remove(item)

    def remove_blacklist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.whitelist.remove(item)


    def __enter__(self) -> Self:
        self.connect()
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.disconnect()

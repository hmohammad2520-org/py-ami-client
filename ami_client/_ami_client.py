import socket, threading
from typing import List, Self, Type

DISCONNECT_OS_ERROR_MESSAGE  =  'An operation was attempted on something that is not a socket'

class AMIClient:
    def __init__(
            self,
            host: str = '127.0.0.1',
            port: int = 5038,
            timeout: int = 10,
            socket_buffer: int = 2048,
        ) -> None:

        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket_buffer = socket_buffer

        from ._registry import Registry
        self.registry = Registry()
        self.connected = False

    def connect(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.thread = threading.Thread(target=self.listen, daemon=True)

        self.connected = True
        self.socket.connect((self.host, self.port))
        self.thread.start()

    def disconnect(self) -> None:
        self.connected = False
        self.socket.close()
        self.thread.join()


    def listen(self) -> None:
        buffer = b''
        try:
            while self.connected:
                try: data = self.socket.recv(self.socket_buffer)
                except TimeoutError: continue
                buffer += data
                while b'\r\n\r\n' in buffer:
                    raw_operation, buffer = buffer.split(b'\r\n\r\n', 1)
                    self.registry._register_new_operation(raw_operation.decode())

        except OSError as e:
            ## This Error message is excepted sometimes and this line prevents random crashes
            if DISCONNECT_OS_ERROR_MESSAGE not in str(e): 
                self.connected = False
                self.socket.close()
                raise e

        except Exception as e:
            self.connected = False
            self.socket.close()
            raise e


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

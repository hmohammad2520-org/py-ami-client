import socket, threading
from typing import List, Type

from .registry import Registry

DISCONECT_OS_ERROR_MESSAGE =  'An operation was attempted on something that is not a socket'

class AMIClient:
    def __init__(
            self,*,
            host: str = '127.0.0.1',
            port: int = 5038,
            timeout: int = 10,
            socket_buffer: int = 2048,
            ) -> None:

        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket_buffer = socket_buffer

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)

        self.action_id: int = 0
        self.connected: bool = False

        self.registry: Registry = Registry()


    def connect(self) -> None:
        self.connected = True
        self.socket.connect((self.host, self.port))
        self.thread = threading.Thread(target=self.listen, daemon=True)
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
                    self.registry.register_operation(raw_operation.decode())


        except OSError as e:
            if not DISCONECT_OS_ERROR_MESSAGE in str(e): 
                self.connected = False
                self.socket.close()
                raise e

        except Exception as e:
            self.connected = False
            self.socket.close()
            raise e


    def add_whitelist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.white_list.add(item)

    def add_blacklist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.black_list.add(item)


    def remove_whitelist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.white_list.remove(item)

    def remove_blacklist(self, items: List[Type]) -> None:
        for item in items:
            self.registry.white_list.remove(item)


    def __enter__(self) -> None:
        self.connect()
    
    def __exit__(self, type, value, traceback) -> None:
        self.disconnect()

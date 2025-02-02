import time, socket, threading
from .exeptions import AMIException
from .operation_handler import OperationHandler

DISCONECT_OS_ERROR_MESSAGE =  'An operation was attempted on something that is not a socket'

class AMIClient:
    def __init__(
            self,*,
            host: str = '127.0.0.1',
            port: int = 5038,
            username: str,
            secret: str,
            timeout: int = 10,
            socket_buffer: int = 2048,
            ) -> None:

        self._host = host
        self._port = port
        self._username = username
        self._secret = secret
        self._timeout = timeout
        self._socket_buffer = socket_buffer

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(self._timeout)

        self._action_id = 0
        self._connected = False

        self.handlers: list[OperationHandler] = [OperationHandler('main')]

    def connect(self) -> None:
        self._connected = True
        self._socket.connect((self._host, self._port))
        self._thread = threading.Thread(target=self.listen, daemon=True)
        self._thread.start()
        self.login()


    def disconnect(self) -> None:
        self._connected = False
        self.logoff()
        self._socket.close()
        self._thread.join()

    def listen(self) -> None:
        buffer = b''
        try:
            while self._connected:
                try: data = self._socket.recv(self._socket_buffer)
                except TimeoutError: continue
                buffer += data
                while b'\r\n\r\n' in buffer:
                    raw_operation, buffer = buffer.split(b'\r\n\r\n', 1)
                    for handler in self.handlers:
                        handler.create_operation(raw_operation)


        except OSError as e:
            if not DISCONECT_OS_ERROR_MESSAGE in str(e): 
                self._connected = False
                self._socket.close()
                raise e

        except Exception as e:
            self._connected = False
            self._socket.close()
            raise e


    def login(self) -> None:
        response = self._send_action('Login',Username=self._username, Secret=self._secret)
        if not response:
            raise TimeoutError('Timeout while Logging in.')

        if not response.get('Response') == 'Success' and response.get('Message') == 'Authentication accepted':
            raise AMIException('Access Deny, Wrong credentials or access is not permited.')


    def logoff(self) -> None:
        self._send_action('logoff')


    def _send_action(self, action_name, **kwargs) -> dict:
        self._action_id += 1

        action_string = f'Action: {action_name}\r\n'
        action_string += f'ActionID: {self._action_id}\r\n'

        for key, value in kwargs.items(): 
            action_string += f'{key}: {value}\r\n'

        action_string += '\r\n'
        self._socket.sendall(action_string.encode())
        Start = time.time()

        while (time.time() - Start) < self._timeout:
            if not self._connected: break
            
            response = self.handlers.get_response(self._action_id)

            if response:
                self.handlers.remove_response(self._action_id)
                return response
            
            # For preventing locking application
            time.sleep(0.05)

        else: raise TimeoutError(f'Timeout while getting response. action: {action_name} - action id: {self._action_id}')


    def __enter__(self) -> None:
        self.connect()
        self.login()
    
    def __exit__(self, type, value, traceback) -> None:
        self.logoff()
        self.disconnect()

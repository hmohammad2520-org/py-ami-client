from classmods import ENVMod
from ami_client import AMIClient
from ami_client.operation.action import CoreStatus
from ami_client.operation.event import VarSet, Newexten

def test_load_env():
    ENVMod.load_dotenv()
    ENVMod.save_example()
    ENVMod.sync_env_file()

def test_create_client():
    ami_client = AMIClient(**ENVMod.load_args(AMIClient.__init__))
    ami_client.add_blacklist([VarSet, Newexten])
    assert ami_client
    return ami_client

def test_connection():
    ami_client = test_create_client()
    ami_client.connect()
    assert ami_client.is_connected()
    ami_client.disconnect()

def test_auth():
    ami_client = test_create_client()
    ami_client.connect()
    ami_client.login()
    assert ami_client.is_authenticated()
    ami_client.disconnect()

def test_core_status():
    ami_client = test_create_client()
    assert ami_client.send_action(CoreStatus())

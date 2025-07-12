import os, dotenv
from ami_client import AMIClient
from ami_client.operation.action import Originate
from ami_client.operation.event import VarSet, Newexten

dotenv.load_dotenv()

ami_client = AMIClient(
    host=os.environ.get('ASTERISK_HOST', '127.0.0.1'),
    port=int(os.environ.get('ASTERISK_PORT', '5038')),
    Username=os.environ.get('ASTERISK_USER'),
    Secret=os.environ.get('ASTERISK_SECRET'),
    AuthType=os.environ.get('ASTERISK_AUTH_TYPE', 'plain'),  #type: ignore
    Key=os.environ.get('ASTERISK_KEY'),
    Events=os.environ.get('ASTERISK_EVENTS', '').split(','),
    timeout=3,
)
ami_client.add_blacklist([VarSet, Newexten])

def test_connection():
    with ami_client:
        assert ami_client.is_connected()

def test_auth():
    with ami_client:
        assert ami_client.is_authenticated()

def test_originate():
    assert Originate(
        ActionID=2,
        Channel="SIP/223",
        Exten="09195613940",
        Context="from-internal",
        Priority="1",
        Timeout="30000",
    ).send(ami_client, close_connection=True)
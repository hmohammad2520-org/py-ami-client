import time
from classmods import ENVMod
from ami_client import AMIClient
from ami_client.operation.event import (
    Event,
    VarSet, Newexten,
    AgentConnect, AgentComplete,
)

ENVMod.load_dotenv()

with AMIClient(**ENVMod.load_args(AMIClient.__init__)) as client:
    client.add_blacklist([VarSet, Newexten])

    @client.on_event(Event)
    def on_all_events(event: Event):
        print(f'New event: {event}')

    @client.on_event(AgentConnect)  #type: ignore
    def on_agent_connect(event: AgentConnect):
        print(f'#### {event.CallerIDNum} calling... ####')

    @client.on_event(AgentComplete)  #type: ignore
    def on_agent_compleate(event: AgentComplete):
        print(f'#### {event.CallerIDNum} completed with {event.DestExten} ####')

    while True:
        try:
            time.sleep(30)
            if not client.is_connected():
                client.connect()
                client.login()

        except KeyboardInterrupt:
            break

        except Exception as e:
            print(e)
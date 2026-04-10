import networking
from node_config import *
import command


def message_received(client, topic, message):
    pass


networking.mqtt_initialize()
networking.mqtt_connect(
    [f"temperature-zone-{i + 1}" for i in range(num_zones)], message_received
)

networking.socket_connect()


def loop():
    demo_command = command.Command(values=["message to secondary through socket"])
    networking.socket_send_message(demo_command)

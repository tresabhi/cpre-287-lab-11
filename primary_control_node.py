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
    demo_command = command.Command(msg="message to secondary through mqqt")
    networking.mqtt_publish_message(networking.TEMP_FEEDS, demo_command)
    # networking.socket_send_message("what on earth is happening")

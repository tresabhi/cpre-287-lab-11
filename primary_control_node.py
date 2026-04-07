import wifi
import socketpool
from secrets import secrets
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import networking
from node_config import *


# Called when an MQTT message is received.
# topic is the feed name the message was published on.
# message is the contents of the message.
def message_received(client, topic, message):
    print(f"New message on topic {topic}: {message}")

    # TODO: Parse the feed name and take action


# TODO: set up networking, subscribe to feeds, and send initial feed messages


# TODO: probably want some global variables here...
networking.connect_to_network()
networking.mqtt_initialize()
networking.mqtt_connect(
    [f"temperature-zone-{i + 1}" for i in range(num_zones)], message_received
)


# Run the regular primary control node tasks
def loop():
    # TODO: throttle this loop? (i.e. don't run it every time)

    # print("Executing primary control node loop")

    # TODO: Main temperature control logic

    pass

import command
from secrets_db import *
import networking
import time
import temperature_measurement_node
import node_config

networking.connect_to_network()

pre_functions = [
    networking.loop,
]
post_functions = []

if node_type == node_config.NODE_TYPE_PRIMARY:
    import primary_control_node

    def send():
        # msg = command.Command(command.TYPE_NONE, [21, 67], "you smart right?")
        networking.socket_send_message("what on earth is happening")

    def run(elapsed_seconds):
        iterations = round(elapsed_seconds * frequency)

        for _ in range(iterations):
            temperature_measurement_node.loop(1 / frequency)

    frequency = 10
    pre_functions.extend([send, primary_control_node.loop])
    post_functions.extend([run])

elif node_type == node_config.NODE_TYPE_SECONDARY:
    import secondary_control_node

    print("zooweemama")

while True:
    start_time = start = time.time()

    for f in pre_functions:
        f()

    end_time = start = time.time()
    elapsed_seconds = end_time - start_time

    for f in post_functions:
        f(elapsed_seconds)

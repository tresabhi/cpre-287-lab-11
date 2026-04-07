import command
from secrets_db import *
import networking
import time
import temperature_measurement_node
import node_config

if node_type == node_config.NODE_TYPE_PRIMARY:
    import primary_control_node

    def send():
        msg = command.Command(command.TYPE_NONE, [21, 67], "you smart right?")
        networking.socket_send_message("what on earth?")

    frequency = 10
    functions = [
        send,
        networking.loop,
        primary_control_node.loop,
    ]

    while True:
        start_time = start = time.time()

        for f in functions:
            f()

        end_time = start = time.time()
        elapsed_seconds = end_time - start_time
        iterations = round(elapsed_seconds * frequency)

        for _ in range(iterations):
            temperature_measurement_node.loop(1 / frequency)
elif node_type == node_config.NODE_TYPE_SECONDARY:
    import secondary_control_node

    print("zooweemama")

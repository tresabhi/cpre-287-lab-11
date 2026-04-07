import primary_control_node
import networking
import time
import temperature_measurement_node

frequency = 10

functions = [
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

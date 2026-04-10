import command
import time
import networking

t0 = None
dts = []
dt_average = None
max_dropped_heatbeats = 3


def listen():
    global t0, dts, dt_average

    if t0 == None:
        t0 = time.monotonic()

    dt = time.monotonic() - t0
    t0 = time.monotonic()

    dts.append(dt)
    dts = dts[-10:]

    dt_average = sum(dts) / len(dts)


def beat():
    beat_command = command.Command(type=command.TYPE_HEARTBEAT, values=[])
    networking.socket_send_message(beat_command)


def loop():
    global dt_average, t0

    if dt_average == None:
        return

    time_since_last = time.monotonic() - t0
    expected_heartbeats = time_since_last / dt_average

    if expected_heartbeats >= max_dropped_heatbeats:
        print(
            f"Other board is probably dead, expected {round(expected_heartbeats)} beats by now"
        )

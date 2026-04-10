import networking
import command
import time

t = None


def listen(message):
    print(message)

    [command_type, *arguments] = message.split(":")
    command_type = int(command_type)

    if t is None:
        t = time.monotonic()
    elif command_type == command.TYPE_HEARTBEAT:
        dt = time.monotonic() - t
        t = time.monotonic()
        print(f"{dt=}")


networking.socket_listen(listen)

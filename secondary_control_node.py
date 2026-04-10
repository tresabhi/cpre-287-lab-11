import networking
import command
import time
import heart


def listen(message):
    [type, *arguments] = message.split(":")
    type = int(type)

    if type == command.TYPE_HEARTBEAT:
        heart.listen()


def loop():
    heart.loop()
    heart.beat()


networking.socket_connect()
networking.socket_listen(listen)

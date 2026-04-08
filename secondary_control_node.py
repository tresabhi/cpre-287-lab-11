import networking


def listen(message):
    print(message)


networking.socket_listen(listen)

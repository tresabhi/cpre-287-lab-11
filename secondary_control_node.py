import networking

networking.socket_connect()


def listen(*args):
    print(args)


networking.socket_listen(listen)

while True:
    pass

import networking

def listen(*args):
    print(args)

networking.socket_listen(listen)

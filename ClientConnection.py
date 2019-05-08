# #!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM

class ClientConnection:
    '''
    
    Usage:
    conn = ClientConnection(('127.0.0.1', 64010))
    with conn as s:
    #conn.__enter__() executes: connection open
    s.send(b'')
    s.send(b'')
    s.send(b'')
    # conn.__exit__() executes: connection closed.

    '''
    def __init__(self,addr,family=AF_INET,type=SOCK_STREAM):
        self.addr = addr
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("A conenction exists.")
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.addr)
        return self.sock


    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

# #!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM

class ClientConnection:
    """
    This class returns a connection object that can be used within the "with" context manger to send and receive message to/from the server.
    """    

    def __init__(self,addr,family=AF_INET,type=SOCK_STREAM):
        """
        This function initalises the client connection. 
        """
        self.addr = addr
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        """ 
        This function checks whether or not a connection exists.
        """
        if self.sock is not None:
            raise RuntimeError("A conenction exists.")
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.addr)
        return self.sock


    def __exit__(self, exc_ty, exc_val, tb):
        """
        This function closes the connection.
        """
        self.sock.close()
        self.sock = None

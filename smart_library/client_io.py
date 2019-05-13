#!/usr/bin/env python3

import socket

class Client:
    """
    Client class for handling client's connection to the server.
    """
    HOST = ''
    PORT = 0

    def __init__(self):
        """
        This function initialises the client and the port they are listening on.
        """
        self.HOST = ''
        self.PORT = 64010 #Port used by the server        

    def connection_establish(self):
        """
        This function establishes the client's connection to the server.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("client started")
            s.connect((self.HOST,self.PORT))
            s.sendall(b'Hellooo WOrldddddd')
            data = s.recv(1024)


    def sending_data():
        """
        This function defines the client sending data to the server.
        """
        pass

# print('Received', repr(data))

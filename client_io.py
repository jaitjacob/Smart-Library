#!/usr/bin/env python3

import socket

class Client:
    HOST = ''
    PORT = 0

    def __init__(self):
        self.HOST = ''
        self.PORT = 64010 #Port used by the server        

    def connection_establish(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("client started")
            s.connect((self.HOST,self.PORT))
            s.sendall(b'Hellooo WOrldddddd')
            data = s.recv(1024)


    def sending_data():
        pass

print('Received', repr(data))

#!/usr/bin/env python3

import socket

class Client:
    HOST = ''
    PORT = 0

    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 64010 #Port used by the server        

    def connection_establish(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("client started")
            s.connect((self.HOST,self.PORT))
            #s.sendall(b'Hellooo WOrldddddd')
            #data = s.recv(1024)
            #print('Received', repr(data))


    def sending_data():
        pass



if __name__ == "__main__":
    client = Client()
    client.connection_establish()

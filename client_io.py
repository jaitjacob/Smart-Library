#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' #Servers hostname or IP address
PORT = 65432 #Port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hellooo WOrldddddd')
    data = s.recv(1024)

print('Received', repr(data))
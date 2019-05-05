#!/usr/bin/env python3

#For now the server is just an echo server. 

import socket

class Server:
    HOST = ''  # Standard loopback interface address (localhost)
    PORT = 0        # Considering non-privileged ports are > 1023

    def __init__(self):
        #self.HOST = socket.gethostbyname(socket.gethostname())
        self.HOST = '127.0.0.1'
        self.PORT = 64010

    def server_listening(self):
        while True:
            print("server running")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.HOST, self.PORT))
                s.listen()
                conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    print(data.decode())
                    if not data:
                        break
                    conn.sendall(data)

    def print_server_info(self):
        print("Server running at " + str(self.HOST) + ":" + str(self.PORT)+".")

if __name__ == "__main__":
    activeServer = Server()
    activeServer.print_server_info()
    activeServer.server_listening()

    

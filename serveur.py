#!/usr/bin/env python
# coding: utf-8

# Pour le UDP : pas pas de send et pour reception
# message il faut utiliser recvfrom() avec l'adresse local
# et le port

import socket
import threading

class newChat(threading.Thread):
    def __init__(self,conn,addr,number):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.number = number

    def run(self):
        print("Hello, client Addr = " + str(self.addr))
        while True:
            msg = self.conn.recv(1024).decode()
            if not msg:
                self.conn.close()
                break;
            elif msg == "stop":
                print("Connection was closed with :" +str(self.addr))
            else:
                print("Client numéro "+str(self.number) +" : " + str(msg))
        

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # pour UDP mettre DGRAM à la place de STREAM
socket.bind(('',7555))
socket.listen(5)
number = 1
while True:
    ClientCon, ClientAddr = socket.accept()
    newChat(ClientCon,ClientAddr,number).start()
    number += 1
    
print("Server socket closed")
socket.close()

#!/usr/bin/env python
# coding: utf-8

# Pas de connect mais un sendto() et un recvfrom()

import socket

host = ""
port = 7555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host,port))
msg = ""
while msg != "stop":
    msg = input()
    socket.send(msg.encode())

print("Client socket closed")
socket.close()

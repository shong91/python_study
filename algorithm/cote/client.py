from socket import *

"""
set client socket
"""

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

message = "I am client"
clientSock.send(message.encode('utf-8'))

message = clientSock.recv(1024) #1024bytes
print('received: ', message.decode('utf-8'))
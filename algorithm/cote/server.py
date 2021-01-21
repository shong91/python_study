# ref: https://seolin.tistory.com/97

from socket import *

"""
set server socket
"""
# 1. create socket
serverSock = socket(AF_INET, SOCK_STREAM)

# 2. bind socket (tuple - address family)
# '' means INADDR_ANY (Broadcast)
serverSock.bind(('', 8080))

# 3. listen : waiting for connection
# parameter = 동시접속cnt. 1 = 하나의 접속만을 허용
serverSock.listen(1)

# 4. accept when connected
connectionSock, addr = serverSock.accept()

message = connectionSock.recv(1024) #1024bytes
print('received: ', message.decode('utf-8'))

message = "I am server. "
connectionSock.send(message.encode('utf-8'))

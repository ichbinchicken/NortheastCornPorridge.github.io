#!/usr/bin/python
from socket import *
from time import *

req_array = []
segments = []
host, port = ('', 80)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((host, port))
serverSocket.listen(1)
print 'Serving HTTP on Port %s ...' % port
while True:
    try:
        clientConnection, clientAddress = serverSocket.accept()
        request = clientConnection.recv(1024)
        print request
        req_array = request.split('\n', 1)
        segments = req_array[0].split()
        f = open(segments[1][1:], 'r')
        content = f.read()
        http_response = 'HTTP/1.1 200 OK\r\n'
        date = ctime()+'\r\n'
        clientConnection.sendall(http_response+date+'\r\n'+content)
        f.close()
        clientConnection.close()
    except IOError: 
        http_response = 'HTTP/1.1 404 Not Found\r\n'
        date = ctime()+'\r\n'
        clientConnection.sendall(http_response+date+'\r\n')
        clientConnection.close()

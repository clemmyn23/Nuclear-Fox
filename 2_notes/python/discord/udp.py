import socket


sock = socket.socket()
sock.bind('', 8080)

for i in range(0,10):
    sock.send('hello world')

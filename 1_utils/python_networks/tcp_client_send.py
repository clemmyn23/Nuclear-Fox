# Clement Ng
import socket

PORT = 9876

print("setting up and connecting")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', PORT))

# message = "hello world this is a long sentence \0\0"
# sock.send(message.encode('utf-8'))
# sock.send(message.encode('utf-8'))
# sock.send(message.encode('utf-8'))

print("enter your messages..")
while True:
    message = input()
    if not message:
        break
    sock.sendto(message.encode('utf-8'), ('', PORT))

sock.close()

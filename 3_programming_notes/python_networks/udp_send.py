import socket

PORT = 9876
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))

while True:
    message = input()
    if not message:
        break
    sock.sendto(message.encode('utf-8'), ('', PORT))

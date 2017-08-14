# Clement Ng
import socket, select
import sys

PORT = 9876
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', PORT))
sock.listen(5)
print("listening")
accepted_sock, b = sock.accept()
print("connection accepted {} {}".format(accepted_sock, b))

print("waiting for msg..")
while True:
    readable, b, c = select.select([accepted_sock], [], [], 0)
    for s in readable:
        data = s.recv(16)
        if data:
            print("> {}".format(data.decode('utf-8')))
        else:
            sock.close()
            sys.exit()

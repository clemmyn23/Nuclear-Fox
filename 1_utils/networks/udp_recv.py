import socket
import select

# tests using select instead of building
# a socket.recv() polling routine from ground-up


PORT = 9876

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

i = 0
blocked = 0
while i < 5:
    readable, b, c = select.select([sock], [], [], 0)
    for s in readable:
        data = s.recv(300)
#         print("data {}".format(data.decode('utf-8')))
        print("data {}".format(data))
#         print("blocked {}".format(blocked))
        i += 1

        blocked = 0

    blocked += 1
sock.close()

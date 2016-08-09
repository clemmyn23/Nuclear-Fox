#!/usr/bin/python3

# z5015618 - Lik Chung (Clement), NG
# COMP3331 - lab02
#
# NOTE: CSE machines use Python3.2.3
# kinda backwards compatable with python2
# ipv4 UDP packet sender and reciever
# also see https://docs.python.org/3.2/library/socket.html

import sys, time, socket

# CONSTANTS
NUM_PACKETS = 10
TIMEOUT = 1


if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except Exception as e:
        print(str(e))
        print("Usage: python3 {} [HOST] [PORT]".format(sys.argv[0]))
        sys.exit(1)


    for i in range(0, NUM_PACKETS):
        try:
            # bind sock to ipv4, UDP. set timeout
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(TIMEOUT)

            # build message and encode to byte-string
            rtt = time.time()
            msg = "PING {} {} \r\n".format(i, rtt).encode('utf-8')

            # send packet
            sock.sendto(msg, (host, port))

            # wait for reply
            recv = sock.recv(128).decode('utf-8').rstrip()
            sock.close()

            # calculate rtt
            rtt = int( (time.time() - rtt)*1000 )
            print("ping to {}, seq = {}, rtt = {} ms".format(host, i, rtt))

            # TODO wait for 1sec delay time-up

        except socket.timeout:
            print("connection timed out")
            # pass
        except Exception as e:
            print("unknown error {}".format(str(e)))

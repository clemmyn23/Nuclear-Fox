#!/usr/bin/python3

# z5015618 - Lik Chung (Clement), NG
# COMP3331 - ass1
#
# NOTE: CSE machines use Python3.2.3

import sys, time, socket
import re
from STP.utils import STP
from STP.utils import STP_header

# CONSTANTS
NUM_PACKETS = 10
TIMEOUT = 1


# This sends the SYN (and then ACK). use connect()


PAYLOAD_MAXSIZE = 1500


if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
        inputfile = ""
        mws = 0
        mss = 0
        timeout = 0
        pdrop = 0
        seed = 0
    except Exception as e:
        print("Usage: python3 {} [HOST] [PORT]".format(sys.argv[0]))
        sys.exit(1)


    # bind sock to ipv4, UDP. set timeout
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect((host, port))
    except Exception as e:
        print("unable to connect to host [] port []".format(host, port))
        sys.exit(1)

    # sock.settimeout(TIMEOUT)
    event = STP.EVENT_handshake
    subevent = STP.SUBEVENT_handshake_SYN

    while True:

        usrinput = input("what to send: ")
        if len(usrinput) == 0:
            continue

        # EVENT 1 - Establishing connection
        elif re.match("SYN", usrinput) != None:
        # if event == STP.EVENT_handshake:
            if subevent = STP.SUBEVENT_handshake_SYN:
                print("sending SYN")
                msg = STP_header(flags=['SYN'])
                sock.send(msg.compile().encode('utf-8'))
                # TODO timeouts
                subevent = STP.SUBEVENT_handshake_SYNACK

            print("waiting for SYNACK")
            elif subevent == STP.SUBEVENT_handshake_SYNACK:
                recv = sock.recvfrom(STP.HEADER_SIZE + PAYLOAD_MAXSIZE)
                header = STP_header(header=recv[0].decode('utf-8')[0:STP.HEADER_SIZE])
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE+1:]

                if 'SYN' in header.flags and 'ACK' in header.flags:
                    subevent = STP.SUBEVENT_handshake_ACK

                    print("sending ACK")
                    msg = STP_header(flags=['ACK'])
                    sock.send(msg.compile().encode('utf-8'))
                    event = STP.EVENT_delivery



        elif re.match("FIN", usrinput) != None:
            msg = "FIN \r\n".encode('utf-8')
            sock.send(msg)

            print("waiting for FIN ACK0")
            recv = sock.recvfrom(128)[0].decode('utf-8').rstrip()
            print("SENDER: {}".format(recv[0]))

            print("sending FIN1")
            sock.send(msg)

            break





        else:
            msg = "MSG {} \r\n".format(usrinput).encode('utf-8')
            sock.send(msg)

            recv = sock.recv(128).decode('utf-8').rstrip()
            print("GOT: {}".format(recv))


    sock.close()
    print("connection closed.")

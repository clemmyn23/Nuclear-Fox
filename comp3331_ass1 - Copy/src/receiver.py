#!/usr/bin/python3

# z5015618 - Lik Chung (Clement), NG
# COMP3331 - ass1
#
# NOTE: CSE machines use Python3.2.3
# also see https://docs.python.org/3.2/library/socket.html

import sys, time, socket
import json
import re
from STP.utils import STP
from STP.utils import STP_header


# This sends the SYNACK. use bind()



PAYLOAD_MAXSIZE = 1500

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        outputfile = ""
    except Exception as e:
        print("Usage: python3 {} [PORT]".format(sys.argv[0]))
        sys.exit(1)

    messagenum = 0

    # bind sock to ipv4, UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind(('', port))
    except Exception as e:
        print("unable to bind socket to port [{}]".format(port))
        sys.exit(1)

    # variables
    event = STP.EVENT_handshake
    subevent = STP.SUBEVENT_handshake_SYN

    src_port = 0
    dst_port = 0
    seq_num = 0
    ack_num = 0
    window_size = 0
    mws = 0

    print("now listening:")

    while True:
        if event == STP.EVENT_handshake:
            if subevent == STP.SUBEVENT_handshake_SYN:

                print("waiting for SYN")
                # recv[0] message, recv[1] ip
                recv = sock.recvfrom(STP.HEADER_SIZE + PAYLOAD_MAXSIZE)
                header = STP_header(header=recv[0].decode('utf-8')[0:STP.HEADER_SIZE])
<<<<<<< HEAD
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE:]
=======
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE+1:]
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817

                if 'SYN' in header.flags:
                    print("sending SYNACK")

                    synack = STP_header(flags=['SYN', 'ACK'])
                    sock.sendto(synack.compile().encode('utf-8'), recv[1])
<<<<<<< HEAD
                    messagenum += 1

=======

                    messagenum += 1
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817
                    subevent = STP.SUBEVENT_handshake_ACK

            elif subevent == STP.SUBEVENT_handshake_ACK:
                print("waiting for ACK")
                recv = sock.recvfrom(STP.HEADER_SIZE + PAYLOAD_MAXSIZE)    # [0] message, [1] ip
                header = STP_header(header=recv[0].decode('utf-8')[0:STP.HEADER_SIZE])
<<<<<<< HEAD
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE:]
=======
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE+1:]
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817

                if 'ACK' in header.flags:
                    print("ACK received. Start accepting payload")
                    event = STP.EVENT_delivery

            else:
                print("STP subevent: this should never happen")
                sys.exit(1)

        elif event == STP.EVENT_delivery:
<<<<<<< HEAD

            print("waiting for payload")
            recv = sock.recvfrom(STP.HEADER_SIZE + PAYLOAD_MAXSIZE)
            header = STP_header(header=recv[0].decode('utf-8')[0:STP.HEADER_SIZE])
            payload = recv[0].decode('utf-8')[STP.HEADER_SIZE:]

            # print("GOT HEADER: {}".format(header.compile()))
            # print("HEADER FLAGS: {}".format(header.flags))

            if not header.flags:
                print("GOT MSG: {}".format(payload))

                print("sending ACK")
                msg = STP_header(flags=['ACK']).compile().encode('utf-8')
                sock.sendto(msg, recv[1])
                messagenum += 1

            elif 'FIN' in header.flags:
                print("GOT: FIN0")
                event = STP.EVENT_termination
                subevent = STP.SUBEVENT_termination_ACK0

                print("sending ACK0")
                msg = STP_header(flags=['ACK']).compile().encode('utf-8')
                sock.sendto(msg, recv[1])
                messagenum += 1

                print("sending FIN1")
                msg = STP_header(flags=['FIN']).compile().encode('utf-8')
                sock.sendto(msg, recv[1])
                messagenum += 1

                print("waiting for ACK1")
                recv = sock.recvfrom(STP.HEADER_SIZE + PAYLOAD_MAXSIZE)
                header = STP_header(header=recv[0].decode('utf-8')[0:STP.HEADER_SIZE])
                payload = recv[0].decode('utf-8')[STP.HEADER_SIZE:]

                if 'ACK' in header.flags:
                    break

            else:
                print("STP delivery: this should never happen")
=======
            print("waiting for payload")
            recv = sock.recvfrom(PAYLOAD_MAXSIZE)    # [0] message, [1] ip
            print(recv[0].decode('utf-8').rstrip())

            if re.match("MSG ", recv[0].decode('utf-8')) != None:
                # print("TODO calculating ACK. TODO payload out of order")
                print("sending ACK")
                sock.sendto("ACK {}".format(messagenum).encode('utf-8'), recv[1])
                messagenum += 1

            elif re.match("FIN ", recv[0].decode('utf-8')) != None:
                print("processing FIN0")
                event = STP.EVENT_termination
                subevent = STP.SUBEVENT_termination_ACK0

                print("sending FIN ACK0")
                sock.sendto("ACK {}".format(messagenum).encode('utf-8'), recv[1])
                messagenum += 1
                subevent = STP.SUBEVENT_termination_FIN1



        elif event == STP.EVENT_termination:
            print("waiting for second FIN1")
            recv = sock.recvfrom(PAYLOAD_MAXSIZE)    # [0] message, [1] ip
            print(recv[0].decode('utf-8').rstrip())

            if re.match("FIN ", recv[0].decode('utf-8')) != None:
                print("sending final ACK. terminating connection")
                sock.sendto("ACK {}".format(messagenum).encode('utf-8'), recv[1])
                messagenum += 1


                break
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817

        else:
            print("STP event: this should never happen")
            sys.exit(1)


    sock.close()
    print("connection closed.")
    print("total datagrams sent: {}".format(messagenum))

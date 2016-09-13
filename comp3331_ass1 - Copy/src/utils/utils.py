#!/usr/bin/python3
import json
class STP:
    EVENT_handshake = 0
    EVENT_delivery = 1
    EVENT_termination = 2

    SUBEVENT_handshake_SYN = 10
    SUBEVENT_handshake_SYNACK = 11
    SUBEVENT_handshake_ACK = 12

    SUBEVENT_termination_FIN0 = 20
    SUBEVENT_termination_ACK0 = 21
    SUBEVENT_termination_FIN1 = 22
    SUBEVENT_termination_ACK1 = 23

    with open('STP/STP_header.json') as f:
        header_template = json.load(f)
    HEADER_SIZE = len(json.dumps(header_template, separators=(',',':')))

    def __init__(self):
        pass



class STP_header:

    PORT_ARGLEN = len("65535")
    PORT_RANGE = 65535
    SEQ_ARGLEN = len("4294967295")
    SEQ_RANGE = 4294967295
    FLAGS_ARGLEN = len("ACK,RST,SYN,FIN,PSH")
    FLAGS_ALL = ['ACK', 'RST', 'SYN', 'FIN', 'PSH']
    WINDOW_ARGLEN = len("65535")
    WINDOW_RANGE = 65535

    def __init__(self, header=None, src_port=0, dst_port=0, seq=0,
<<<<<<< HEAD
            ack=0, flags=[], window_size=0):
=======
            ack=0, flags="", window_size=0):
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817
        """Depending on whether header arg is specified,
        on header==None create an empty STP_header object with other args.
        on header!=str  loads the json string into STP_header object.
        """

        if header != None:
            header = json.loads(header)
            self.src_port = int(header['header']['src_port'])
            self.dst_port = int(header['header']['dst_port'])
            self.seq = int(header['header']['seq'])
            self.ack = int(header['header']['ack'])
<<<<<<< HEAD
            self.window_size = header['header']['window_size']
            self.flags = [x.strip() for x in header['header']['flags'].split(',')]
            if '' in self.flags:
                self.flags.remove('')
=======
            self.flags = [x.strip() for x in header['header']['flags'].split(',')]
            self.window_size = header['header']['window_size']
>>>>>>> 2d4b7b795e753940fc217b8a11643ef5f5683817

        else:
            self.src_port = src_port
            self.dst_port = dst_port
            self.seq = seq
            self.ack = ack
            self.flags = flags
            self.window_size = window_size


    def setFields(self, src_port=None, dst_port=None, seq=None,
            ack=None, flags=None, window_size=None):
        """Sets STP_header fields if specified"""

        if src_port != None:
            self.src_port = src_port
        if dst_port != None:
            self.dst_port = dst_port
        if seq != None:
            self.seq = seq
        if ack != None:
            self.ack = ack
        if flags != None:
            self.flags = flags
        if window_size != None:
            self.window_size = window_size


    def compile(self):
        """Compiles the STP_header object into a fixed length string"""

        head = {}
        head['header'] = {}
        head['header']['src_port'] = str(self.src_port).rjust(STP_header.PORT_ARGLEN, '0')
        head['header']['dst_port'] = str(self.dst_port).rjust(STP_header.PORT_ARGLEN, '0')
        head['header']['seq'] = str(self.seq).rjust(STP_header.SEQ_ARGLEN, '0')
        head['header']['ack'] = str(self.ack).rjust(STP_header.SEQ_ARGLEN, '0')
        head['header']['flags'] = (','.join(map(str, self.flags))).ljust(STP_header.FLAGS_ARGLEN, ' ')
        head['header']['window_size'] = str(self.window_size).rjust(STP_header.WINDOW_ARGLEN, '0')

        packed = json.dumps(head, separators=(',',':'))

        if len(packed) != STP.HEADER_SIZE:
            raise Exception("Unable to compile header. Check all fields")
        return json.dumps(head, separators=(',',':'))

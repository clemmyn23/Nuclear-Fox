import sys
# import heapq
from heapq import *

buff = []

heappush(buff, (2, "hello"))
heappush(buff, (1, "cat"))
heappush(buff, (3, "world"))

print("buff: {}".format(buff))
print("peek hq: {}".format(buff[0]))

print("heappop1: {}".format(heappop(buff)))
print("heappop2: {}".format(heappop(buff)))
print("heappop3: {}".format(heappop(buff)))
print("is hq empty: {}".format(not len(buff)))


sys.exit(1)

import queue

buff = queue.PriorityQueue()

buff.put((2, "hello"))
buff.put((1, "cat"))
buff.put((3, "world"))

print("peeking: {}".format(buff[0]))

popped = buff.get()
print("popped: {}".format(popped))

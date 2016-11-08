import threading
import sys
import time


timeout = 500 /1000	# x /1000 seconds = x ms
print("starto")

# this is the timer marker
# will be modified to True after [timeout] ms by Timer thread

isTimerExpired = False

######################
def expiryMarker():
	global isTimerExpired
	isTimerExpired = True


######################
t = threading.Timer(timeout, expiryMarker).start()

while True:
	if isTimerExpired:
		print("operation timeout")
		break
	else:
		# do socket recv here with some tiny socket.timeout
		print(".", end='')
		time.sleep(0.1)

print("finito")
sys.exit(0)




import threading
import time

def printer():
    print("hello")

def main():
    nums = 15

    for i in range(1, nums):
        threading.Timer(1, printer).start()  # seconds, func, args=[], kwargs={}


if __name__ == "__main__":
    main()
    time.sleep(3)

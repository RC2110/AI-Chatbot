from threading import *
import time


# creating a function
def thread_1():
    for i in range(10):
        print('this is thread T')
        # time.sleep(3)


# creating a thread
T = Thread(target=thread_1)

# change T to daemon
T.daemon= True

# starting of Thread T
T.start()
time.sleep(5)
print('this is Main Thread')
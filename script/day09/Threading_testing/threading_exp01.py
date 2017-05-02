import threading
import time
import random

def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 3:
            print('\033[42;1m--green light on---\033[0m')
        elif count < 6:
            print('\033[43;1m--yrllow light on---033[0m')
        elif count < 9:
            if event.isSet():
                event.clear()
            print('\033[41;1m--read light on---\033[0m')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if event.isSet():
            print("car [%s] runing" % n)
        else:
            print("car [%s] waiting" % n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()
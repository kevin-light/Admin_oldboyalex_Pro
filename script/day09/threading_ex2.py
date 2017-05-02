import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("runint task",self.n)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()

t1.join()
t2.join()
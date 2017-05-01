import time


def timer(fun):

    def warpper(*args,**kwargs):

        start_time = time.time()

        fun()
        stop_time = time.time()
        print('the fun run toe %s' % stop_time-start_time)

@timer

def test1():
    time.sleep(3)
    print('int the test1')
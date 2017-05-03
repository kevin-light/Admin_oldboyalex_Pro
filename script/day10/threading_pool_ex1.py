from  multiprocessing import Process, Pool
import time
import os


def Foo(i):
    time.sleep(1)
    print("in process",os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':

    pool = Pool(3)

    for i in range(10):

        #pool.apply_async(func=Foo, args=(i,), callback=Bar)  #callback=回调
        # pool.apply(func=Foo, args=(i,))
        pool.apply_async(func=Foo, args=(i,))

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭
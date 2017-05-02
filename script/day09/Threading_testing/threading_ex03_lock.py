import threading,time

def run(n):

    lock.acquire()
    global number
    number += 1
    time.sleep()
    lock.release()

lock = threading.Lock()
number = 0
t_objs = []
for i in range(100):
    t = threading.Thread(target=run,args=("t-%s" % i,))
#    t.setDaemon(True) #把当前线程设为守护线程，必须在start前设置
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("------all threads has finished...",threading.current_thread(),threading.active_count()) #当前线程

print("number: %s" % number)
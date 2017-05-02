import threading,time

def run(n):

    print("task...",n)
    time.sleep(1)

start_time = time.time()
t_objs = []
for i in range(9):
    t = threading.Thread(target=run,args=("t-%s" % i,))
    t.setDaemon(True) #把当前线程设为守护线程，必须在start前设置
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("------all threads has finished...",threading.current_thread(),threading.active_count()) #当前线程
print("cost:",time.time() - start_time)
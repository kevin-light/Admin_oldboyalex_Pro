import threading,time

def run(n):

    print("task...",n)
    time.sleep(1)

start_time = time.time()
t_objs = []
for i in range(6):
    t = threading.Thread(target=run,args=("t-%s" % i,))

    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("cost:",time.time() - start_time)
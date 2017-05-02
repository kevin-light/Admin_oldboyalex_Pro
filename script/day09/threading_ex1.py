import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)

start_time = time.time()
t_objs = []
for i in range(7):
    t = threading.Thread(target=run,args=("t%s" %i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("cost:",time.time() - start_time)
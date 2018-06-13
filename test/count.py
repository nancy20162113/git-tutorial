#author='zhy'
import threading
import queue

myqueue=queue.Queue()
threadlist=[]
allnum=0
def tongji(path):
    file=open(path,"r")
    l1=file.readlines()
    num=len(l1)
    print(threading.current_thread().name,num)
    myqueue.put(num)
    file.close()

for i in range(5):
    t=threading.Thread(target=tongji,args=(str(i)+".txt",))
    t.start()
    threadlist.append(t)

for t in threadlist:
    t.join()

while not myqueue.empty():
    allnum+=myqueue.get()

print(allnum)




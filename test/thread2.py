#author='zhy'
import threading
import time

def goevent():
    e=threading.Event()
    def go():
        for i in range(10):
            e.wait()
            print(i,"go")
            e.clear()
    threading.Thread(target=go).start()
    return e


t=goevent()
for i in range(10):
    time.sleep(2)
    t.set()


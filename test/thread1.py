#author='zhy'
import threading
import time

def goevent():
    e=threading.Event()
    def go():
        e.wait()
        e.clear()
        print("go")
    threading.Thread(target=go).start()
    return e


t=goevent()
time.sleep(5)
t.set()



import threading
import time
import queue 

#自訂生產者執行緒類別
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue
        #在佇列尾部附加元素
        myqueue.put(self.getName())
        print(self.getName(), ' put ', self.getName(), ' to queue.')

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue
        #在佇列頭部取得元素
        print(self.getName(), ' get ', myqueue.get(), ' from queue.')

myqueue = queue.Queue()

#建立生產者執行緒和消費者執行緒
plist = []
clist = []
for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

#依序啟動生產者執行緒和消費者執行緒
for p, c in zip(plist, clist):
    p.start()
    p.join()
    c.start()
    c.join()

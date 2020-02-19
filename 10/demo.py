import threading

#自訂執行緒類別
class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
        
    def run(self):
        global myevent
        #根據Event物件是否已設定，做出不同的回應
        if myevent.isSet():
            #清除標誌
            myevent.clear()
            #等待
            myevent.wait()
            print(self.getName()+' set')
        else:
            print(self.getName()+' not set')
            #設定標誌
            myevent.set()

myevent = threading.Event()
#設定標誌
myevent.set()

for i in range(10):
    t = mythread(str(i))
    t.start()

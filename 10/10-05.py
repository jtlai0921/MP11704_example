import threading
from random import randint
from time import sleep

#自訂生產者執行緒類別
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            #取得鎖
            con.acquire()
            #假設共用列表中，最多只能容納20個元素
            if len(x) == 20:
                #如果共用列表已滿，生產者等待
                con.wait()
                print('Producer is waiting.....')
            else:
                print('Producer:', end=' ')
                #產生新元素，附加至共用列表
                x.append(randint(1, 1000))
                print(x)
                sleep(1)
                #喚醒等待條件的執行緒
                con.notify()
            #釋放鎖
            con.release()
        
#自訂消費者執行緒類別
class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name =threadname)
    def run(self):
        global x
        while True:
            #取得鎖
            con.acquire()
            if not x:
                #等待
                con.wait()
                print('Consumer is waiting.....')
            else:
                print(x.pop(0))
                print(x)
                sleep(2)
                con.notify()
            con.release()
        
#建立Condition物件，以及生產者執行緒和消費者執行緒
con = threading.Condition()
x = []
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
c.start()
p.join()
c.join()

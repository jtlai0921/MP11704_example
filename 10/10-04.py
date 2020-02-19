import threading
import time

#自訂執行緒類別
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    #重寫run()方法
    def run(self):
        global x
        #取得鎖，如果成功則進入臨界區
        lock.acquire()
        x = x+3
        print(x)
        #退出臨界區，釋放鎖
        lock.release()
        
lock = threading.RLock()
#也可以使用Lock類別實現加鎖和執行緒同步
#lock = threading.Lock()

#存放多個執行緒的列表
tl = []
for i in range(10):
    #建立執行緒並加入列表
    t = mythread()
    tl.append(t)

#多個執行緒互斥存取的變數
x = 0
#啟動列表的所有執行緒
for i in tl:
    i.start()

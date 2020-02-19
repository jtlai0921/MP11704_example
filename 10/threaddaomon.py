import threading
import time

class mythread(threading.Thread):	#繼承Thread類別，建立自訂的執行緒類別
    def __init__(self, num, threadname):
        threading.Thread.__init__(self, name=threadname)
        self.num = num
    def run(self): 				#重寫run()方法
        time.sleep(self.num)
        print(self.num)

t1 = mythread(1, 't1')	#建立自訂執行緒類別物件，daemon預設為False
t2 = mythread(5, 't2')
t2.daemon = True		#設定執行緒物件t2的daemon屬性為True
print(t1.daemon)
print(t2.daemon)
t1.start()			#啟動執行緒
t2.start()

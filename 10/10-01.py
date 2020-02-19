from threading import Thread
import time

def func1(x, y):
    for i in range(x, y):
        print(i, end=' ')
    print()
    time.sleep(10)		#等待10秒

t1 = Thread(target=func1, args=(15, 20))	#建立執行緒物件，args是傳遞給函數的參數
t1.start()			#啟動執行緒
t1.join(5)			#等待中的執行緒t1執行結束，或等待5秒鐘
t2 = Thread(target=func1, args=(5, 10))
t2.start()

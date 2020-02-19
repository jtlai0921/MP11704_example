from threading import Thread
import time
def func1():
    time.sleep(10)

t1 = Thread(target=func1)
print('t1:',t1.isAlive())	#執行緒未未運行，返回False
t1.start()
print('t1:',t1.isAlive())	#執行緒還在運行，返回True
t1.join(5)				#join()方法因逾時而結束
print('t1:',t1.isAlive())	#執行緒還在運行，返回True
t1.join()					#等待中的執行緒結束
print('t1:',t1.isAlive())	#執行緒已結束，返回False

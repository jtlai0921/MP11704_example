from multiprocessing import Process
import os

def f(name):
    print('module name:', __name__)
    print('parent process:', os.getppid())	#查看父處理序ID
    print('process id:', os.getpid())		#查看目前處理序ID
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))	#建立處理序
    p.start()			#啟動處理序
    p.join()			#等待處理序執行結束

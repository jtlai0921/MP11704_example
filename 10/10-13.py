from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()			#取得鎖
    try:
        print('hello world', i)
    finally:
        l.release()		#釋放鎖

if __name__ == '__main__':
    lock = Lock()		#建立鎖物件
    for num in range(10):
        Process(target=f, args=(lock, num)).start()

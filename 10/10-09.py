import multiprocessing as mp

def foo(q):
    q.put('hello world!')			#把資料放入佇列

if __name__ == '__main__':
    mp.set_start_method('spawn')	#Windows系統建立子處理序的預設方式
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))  #建立處理序，把Queue物件作為參數傳遞
    p.start()
    p.join()
    print(q.get())				#從佇列取得資料

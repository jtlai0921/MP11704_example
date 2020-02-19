from multiprocessing import Process, Pipe

def f(conn):
    conn.send('hello world')		#對管道傳送資料
    conn.close()				#關閉管道

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()	#建立管道物件
    p = Process(target=f, args=(child_conn,))	#將管道的一方作為參數，傳遞給子處理序
    p.start()
    p.join()
    print(parent_conn.recv())		#透過管道的另一方取得資料
    parent_conn.close()

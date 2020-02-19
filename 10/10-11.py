from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = a[i]*a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)					#實數
    arr = Array('i', range(10))			#整數型陣列
    p = Process(target=f, args=(num, arr))	#建立處理序物件
    p.start()
    p.join()
    print(num.value)
    print(arr[:])

from multiprocessing import Pool
from statistics import mean

def f(x):
    return mean(x)

if __name__ == '__main__':
    x = [list(range(10)), list(range(20,30)), list(range(50,60)), list(range(80,90))]
    with Pool(5) as p:		#建立包含5個處理序的處理序池
        print(p.map(f, x))		#並行執行

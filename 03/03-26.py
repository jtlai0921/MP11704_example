from random import randint
from math import sqrt

def factoring(n):
    '''對大數進行質因數分解'''
    if not isinstance(n, int):
        print('You must give me an integer')
        return
    #開始分解，把所有質因數都加到result列表
    result = []
    for p in primes:
        while n!=1:
            if n%p == 0:
                n = n/p
                result.append(p)
            else:
                break
        else:
            result = map(str, result)
            result = '*'.join(result)
            return result
    #考慮參數本身就是質數的情況
    if not result:
        return n

testData = [randint(10, 100000) for i in range(50)]
#亂數中的最大數
maxData = max(testData)
#小於maxData的所有質數
primes = [ p for p in range(2, maxData) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]

for data in testData:
    r = factoring(data)
    print(data, '=', r)
    #測試分解結果是否正確
    print(data==eval(r))

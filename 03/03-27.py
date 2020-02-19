from functools import reduce
from math import gcd

def isCoPrime(p):
    '''判斷p中每個元組的第1個數（即mi）之間是否互為質數'''
    for index, item1 in enumerate(p):
        for item2 in p[index+1:]:
            if gcd(item1[0], item2[0])!=1:
                return False
    return True

def extEuclid(Mi, mi):
    '''暴力窮舉法，求Mi對mi的乘法逆元，也可擴展歐幾里得演算法快速求解'''
    for i in range(1, mi):
        if i*Mi % mi == 1:
            return i

def chineseRemainder(p):
    '''p為[(3, 2), (7, 1), (13, 5),(mi, ai) ...]形式的參數，其中3/7/13為商，2/1/5為餘數'''
    #先判斷資料中的mi是否互為質數，如果不是則提示資料錯誤並退出
    if not isCoPrime(p):
        return 'Data error.'        
    #切片淺複製，臨時變數，防止修改實參中的資料
    pp = p[:]
    #求M=m1*m2*m3*...*mn
    ppp = [item[0] for item in pp]
    M = reduce(lambda x,y: x*y, ppp)
    for index, item in enumerate(pp):
        Mi = int(M/item[0])
        bi = extEuclid(Mi, item[0])
        pp[index] = item+(Mi, bi)
    #求解最終結果，sum(ai*bi*Mi) mod M
    result = sum([item[1]*item[2]*item[3] for item in pp])
    result = result % M
    #考慮特殊情況，不允許結果為1
    if result==1:
        result = result+M
    return result

data = [[(3,2), (5,3), (7,2)],
        [(5,1), (3,2)],
        [(5,1), (3,1)],
        [(5,4), (3,2)],
        [(7,2), (8,4), (9,3)],
        [(5,2), (6,4), (7,4)],
        [(3,2), (5,3), (7,4)]]
for p in data:
    print(p)
    print(chineseRemainder(p))

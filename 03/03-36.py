from random import randint
from itertools import permutations

#4個數字和2個運算子可能組成的運算式形式
exps = ('((%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)', 
        '(%s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = r'+-*/'

def test24(v):
    result = []
    #Python允許函數的巢狀定義
    #這個函數對字串運算式求值，並驗證是否等於24
    def check(exp):
        try:
            #有可能會出現除0異常，所以放到異常處理結構中
            return int(eval(exp)) == 24
        except:
            return False
    #全排列，列舉4個數所有可能的順序
    for a in permutations(v):
        #找尋4個數的目前排列能實現24的運算式
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps if check(exp %(a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.append(t)
    return result

for i in range(20):
    print('='*20)
    #產生亂數進行測試
    lst = [randint(1, 14) for j in range(4)]
    r = test24(lst)
    if r:
        print(r)
    else:
        print('No answer for ', lst)

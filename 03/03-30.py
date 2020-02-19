def conv(lst1, lst2):
    '''計算兩個列表所表示的訊號的摺積，並返回一個列表'''
    result = []
    #翻轉第一個列表
    lst1.reverse()
    length1 = len(lst1)
    length2 = len(lst2)
    #移動翻轉後的第一個列表，直到“「完全移入”」
    for i in range(1, length1+1):
        t = lst1[length1-i:]
        #計算重疊“「面積”」
        v = sum((item1*item2 for item1, item2 in zip(t,lst2)))
        result.append(v)
    #繼續移動翻轉後的第一個列表，直到“「完全移出”」
    for i in range(1, length2):
        t = lst2[i:]
        v = sum((item1*item2 for item1, item2 in zip(lst1,t)))
        result.append(v)
    return result

def mul(lst):
    '''把列表中的數字轉換為普通整數的形式'''
    result = ''
    c = 0
    for item in lst[::-1]:
        item = item + c
        #計算目前位數的餘數，以及向前一位進位的數字
        n, c = str(item%10), item //10
        #使用字串記錄臨時結果
        result += n
    if c:
        result += str(c)
    return eval(result[::-1])

def main(num1, num2):
    lst1 = list(map(int, str(num1)))
    lst2 = list(map(int, str(num2)))
    result = conv(lst1, lst2)
    print(mul(result)==num1*num2)

from random import randint
for i in range(100):
    num1 = randint(1, 99999999)
    num2 = randint(1, 99999999999)
    main(num1, num2)

def isValid(s, col):
    '''本函數用來檢查最後一個皇后的位置是否合法'''
    #目前皇后的行號
    row = len(s)
    #檢查目前的皇后們是否有衝突
    for r, c in enumerate(s):
        #如果該列已有皇后，或者某個皇后與目前皇后的水平與垂直距離相等
        #就表示目前皇后的位置不合法，不允許放置
        if c == col or abs(row - r) == abs(col - c):
            return False
 
    return True
 
def queen(n, s=()):
    '''本函數返回的結果是每個皇后所在的列號'''
    #已是最後一個皇后，保存本次結果
    if len(s) == n:
        return [s]
 
    res = []
    for col in range(n):
        if not isValid(s, col): continue
        for r in queen(n, s + (col,)):
            res.append(r)
 
    return res

#形式轉換，最終結果中包含每個皇后所在的行號和列號
result = [[(r, c) for r, c in enumerate(s)] for s in queen(8)]
#輸出合法結果的數量
print(len(result))
#輸出所有可能的結果，也就是所有皇后的擺放位置
#結果中每個皇后的位置是一個元組，裡面兩個數字分別是行號和列號
for r in result:
    print(r)

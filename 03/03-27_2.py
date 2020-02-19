def chineseRemainder(p):
    '''p為[(3, 2), (7, 1), (13, 5), ...]形式的參數，其中3/7/13為商，2/1/5為餘數'''
    #檢查資料是否合法，若有相同商對應至不同餘數，則認為給的資料不合法
    for index1, pair1 in enumerate(p):
        for pair2 in p[index1+1:]:
            if pair1[0]==pair2[0] and pair1[1]!=pair2[1]:
                print('Data Error.')
                return
    #對給定資料按商從大到小排序
    p = sorted(p, key=lambda x:x[0], reverse=True)
    #產生巢狀列表
    possibleValues = list(map(lambda x: list((i*x[0]+x[1] for i in range(1,10000))), p))
    #尋找第一個共同包含的數，該數即為符合條件的最小數
    for value in possibleValues[0]:
        flag = True
        for rest in possibleValues[1:]:
            if value not in rest:
                flag = False
        if flag:
            print(value)
            return
    else:
        print('Can not find a number')

p = [[(5,3), (9,3), (13,3),(17,3)],
     [(9,7), (5,2), (4,3)],
     [(3,2), (5,3), (7,2)],
     [(3,2), (4,1)],
     [(2,1), (4,3), (5,2), (7,3), (9,4)],
     [(2,1), (3,2), (5,4), (6,5), (7,0)]]
for pp in p:
    chineseRemainder(pp)

from itertools import cycle

def demo(lst, k):
    #切片，以免影響原來的資料
    t_lst = lst[:]
    #遊戲一直進行到只剩下最後一個人
    while len(t_lst)>1:
        #建立cycle物件
        c = cycle(t_lst)
        #從1到k報數
        for i in range(k):
            t = next(c)
        #一個人出局，圈子縮小
        index = t_lst.index(t)
        t_lst = t_lst[index+1:] + t_lst[:index]
        #測試用，查看每次一個人出局之後剩餘人數的編號
        print(t_lst)
    #遊戲結束
    return t_lst[0]

lst = list(range(1,11))
print(demo(lst, 3))

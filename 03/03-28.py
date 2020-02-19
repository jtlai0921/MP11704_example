import random

def hongbao(total, num):
    #total表示擬發紅包的總金額
    #num表示擬發紅包的數量
    each = []
    #已發紅包總金額
    already = 0
    for i in range(1, num):
        #為目前搶紅包的人隨機分配金額
        #至少給剩下的每個人留一分錢
        t = random.randint(1, (total-already)-(num-i))
        each.append(t)
        already = already+t
    #剩餘所有的錢發給最後一個人
    each.append(total-already) 
    return each

if __name__=='__main__':
    total = 5
    num = 5
    #模擬30次
    for i in range(30):
        each = hongbao(total, num)
        print(each) 

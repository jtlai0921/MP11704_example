import random

def demo(x, n):
    if n not in x:
        print(n, ' is not an element of ', x)
        return

    i = x.index(n)			#取得指定元素在列表中的索引
    x[0], x[i] = x[i], x[0]	#將指定元素與第0個元素交換
    key = x[0]
    
    i = 0
    j = len(x) - 1
    while i<j:
        while i<j and x[j]>=key:	#由後向前尋找第一個比指定元素小的元素
            j -= 1
        x[i] = x[j] 
        
        while i<j and x[i]<=key:	#由前向後尋找第一個比指定元素大的元素
            i += 1
        x[j] = x[i]
        
    x[i] = key

x =list(range(1, 10))
random.shuffle(x)			#打亂元素的順序
print(x)
demo(x, 4)
print(x)

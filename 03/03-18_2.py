def demo(lst, k):
    temp = lst[:]
    for i in range(k):
        temp.append(temp.pop(0))
    return temp

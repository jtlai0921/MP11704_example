def demo(lst, k):
    x = lst[:k]
    x.reverse()
    y = lst[k:]
    y.reverse()
    r = x+y
    return list(reversed(r))

lst = list(range(1, 21))
print(lst)
print(demo(lst, 5))

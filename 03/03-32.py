def demo(v, n):
    assert 0<v<10, 'v must between 1 and 9'
    assert type(n)==int, 'n must be integer'
    result, t = 0, 0
    for i in range(n):
        t = t*10 + v
        result += t
    return result

print(demo(3, 4))

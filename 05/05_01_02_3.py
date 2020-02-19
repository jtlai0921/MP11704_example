import timeit

#使用列表推導式產生10000個字串
strlist = ['This is a long string that will not keep in memory.' for n in range(10000)]

#使用字串物件的join()方法連接多個字串
def use_join():
    return ''.join(strlist)

#使用運算子+連接多個字串
def use_plus():
    result = ''
    for strtemp in strlist:
        result = result+strtemp
    return result

if __name__ == '__main__':
    #重複執行次數
    times = 1000
    jointimer = timeit.Timer('use_join()', 'from __main__ import use_join')
    print('time for join:', jointimer.timeit(number=times))
    plustimer = timeit.Timer('use_plus()', 'from __main__ import use_plus')
    print('time for plus:', plustimer.timeit(number=times))

def main(n):
    '''參數n表示數字的位元數，例如n=3時，返回495'''
    #待測試數字範圍的起點和結束值
    start = 10**(n-1)+2
    end = start*10-20
    #依序測試每位數
    for i in range(start, end):
        i = str(i)
        #由這幾個數字組成的最大數
        big = ''.join(sorted(i,reverse=True))
        big = int(big)
        #由這幾個數字組成的最小數
        little = ''.join(sorted(i))
        little = int(little)
        if big-little==int(i):
            print(i)
n = 4
main(n)

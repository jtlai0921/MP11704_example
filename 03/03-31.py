from random import randint

def guess():
    #隨機產生一個整數
    value = randint(1,1000)
    #最多允許猜5次
    maxTimes = 5
    for i in range(maxTimes):
        prompt = 'Start to GUESS:' if i==0 else 'Guess again:'
        #加上異常處理結構，防止輸入不是數字的情況
        try:
            x = int(input(prompt))
            #猜對了
            if x == value:
                print('Congratulations!')
            elif x > value:
                print('Too big')
            else:
                print('Too little')
        except:
            print('Must input an integer between 1 and 999')
    else:
        #次數用完還沒猜對，遊戲結束，提示正確答案
        print('Game over. FAIL.')
        print('The value is ', value)

guess()

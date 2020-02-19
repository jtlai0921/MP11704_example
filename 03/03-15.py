from math import pi as PI

def CircleArea(r):
    if isinstance(r, (int, float)): 	#確保接收的參數為數值
        return PI*r*r
    else:
        print('You must give me an integer or float as radius.')

print(CircleArea(3))

from string import ascii_letters
from random import choice
from time import time

letters = ''.join([choice(ascii_letters) for i in range(999999)])
def positions_of_character(sentence, ch):	#使用字串物件的find()方法
    result = []
    index = 0
    index = sentence.find(ch, index+1)
    while index != -1:
        result.append(index)
        index = sentence.find(ch, index+1)
    return result

def demo(s, c):		#普通方法，逐個字元比較
    result = []
    for i,ch in enumerate(s):
        if ch == c:
            result.append(i)
    return result

start = time()
positions = positions_of_character(letters, 'a')
print(time()-start)

start = time()
p = demo(letters, 'a')
print(time()-start)

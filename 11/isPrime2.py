import time

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if not n&1:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n%i == 0:
            return False
    return True

num = 0
start = time.time()
for n in range(100000000):
    if isPrime(n):
        num += 1
print(num)
print(time.time()-start)

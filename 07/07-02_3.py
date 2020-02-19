from time import time

class Timer(object):
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, *args):
        self.end = time()
        self.seconds = self.end-self.start

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+2):
        if n%i == 0:
            return False
    return True

with Timer() as t:
    for i in range(1000):
        isPrime(99999999999999999999999)
print(t.seconds)

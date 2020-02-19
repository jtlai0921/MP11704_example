from memory_profiler import profile

@profile				#修飾器
def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+2):
        if n%i == 0:
            return False
    return True

isPrime(99999999999999999999999)

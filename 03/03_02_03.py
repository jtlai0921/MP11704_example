import time
digits = (1, 2, 3, 4)

start = time.time()
for i in range(1000):
    result = []
    for i in digits:
        for j in digits:
            for k in digits:
                result.append(i*100+j*10+k)
print(time.time()-start)

start = time.time()
for i in range(1000):
    result = []
    for i in digits:
        i = i*100
        for j in digits:
            j = j*10
            for k in digits:
                result.append(i+j+k)
print(time.time()-start)

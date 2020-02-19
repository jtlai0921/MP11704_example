import time
import math

start = time.time()						#取得目前時間
for i in range(10000000):
    math.sin(i)
print('Time Used:', time.time()-start)	#輸出所耗時間

loc_sin = math.sin
start = time.time()
for i in range(10000000):
    loc_sin(i)
print('Time Used:', time.time()-start)

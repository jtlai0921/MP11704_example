import os
import sys

def Reduce(targetFile):
    result = {}
    for line in sys.stdin:		#從標準控制台中獲取得中間結果資料
        riqi, shuliang = line.strip().split(',')
        result[riqi] = result.get(riqi, 0)+1
    with open(targetFile, 'w') as fp:
        for k,v in result.items():
            fp.write(k + ':' + str(v) + '\n')
Reduce('result.txt')

import os
import re
import threading
import time

def Map(sourceFile):				#這段程式碼僅適用於配套檔案，
    if not os.path.exists(sourceFile):	#或者類似的Windows升級日誌
        print(sourceFile, ' does not exist.')
        return    
    pattern = re.compile(r'[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}')
    result = {}
    with open(sourceFile, 'r') as srcFile:
        for dataLine in srcFile:
            r = pattern.findall(dataLine)	#找尋符合日期格式的字串
            if r:
                result[r[0]] = result.get(r[0], 0) + 1
    desFile = sourceFile[0:-4] + '_map.txt'
    with open(desFile, 'a+') as fp:		#中間的臨時結果
        for k, v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    desFolder = 'test'
    files = os.listdir(desFolder)
    def Main(i):					#使用多執行緒
        Map(desFolder + '\\' + files[i])
    fileNumber = len(files)
    for i in range(fileNumber):
        t = threading.Thread(target = Main, args =(i,))
        t.start()    

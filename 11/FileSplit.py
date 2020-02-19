import os
import os.path
import time

def FileSplit(sourceFile, targetFolder):
    if not os.path.isfile(sourceFile):		#原始檔案必須存在
        print(sourceFile, ' does not exist.')
        return
    if not os.path.isdir(targetFolder):		#目的資料夾不存在，則建立
        os.mkdir(targetFolder)
    tempData = []		#存放臨時資料
    number = 1000		#切分後的每個小檔案包含1000列
    fileNum = 1			#切分後的檔案編號
    with open(sourceFile, 'r') as srcFile:
        dataLine = srcFile.readline().strip()
        while dataLine:
            for i in range(number):			#讀取1000列文字
                tempData.append(dataLine) 
                dataLine = srcFile.readline() 
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder, sourceFile[0:-4] + str(fileNum) + '.txt')
            with open(desFile, 'a+') as f:	#建立一個小檔案
                f.writelines(tempData)
            tempData = []
            fileNum = fileNum + 1			#小檔案編號加1

if __name__ == '__main__':
    sourceFile = 'test.txt'				#指定原始檔案
    targetFolder = 'test'					#指定存放切分後，小檔案的資料夾
    FileSplit(sourceFile, targetFolder)

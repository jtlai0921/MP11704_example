from os.path import isdir, join, splitext
from os import remove, listdir
import sys

filetypes = ['.tmp', '.log', '.obj', '.txt']	#指定要刪除的檔案類型

def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)			#遞迴呼叫
        elif splitext(temp)[1] in filetypes:	#檢查檔案類型
            remove(temp)					#刪除檔案
            print(temp, ' deleted....')

def main():
    directory = r'c:\windows\temp'
    #directory = sys.argv[1]
    delCertainFiles(directory)

main()

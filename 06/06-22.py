from os.path import isdir, join
from os import listdir

AllLines = []				#儲存所有程式碼
NotRepeatedLines = []		#保存不重複的程式碼行列
file_num = 0				#檔案數量
code_num = 0 				#程式碼總列數

def LinesCount(directory):
    global AllLines
    global NotRepeatedLines
    global file_num
    global code_num

    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):			#遞迴遍歷子資料夾
            LinesCount(temp)
        elif temp.endswith('.cpp'):	#只考慮.cpp 檔案
            file_num += 1
            with open(temp, 'r') as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    if line not in NotRepeatedLines:
                        NotRepeatedLines.append(line)	#記錄非重複列
                    code_num += 1		#記錄所有程式碼列
path = r'D:\Code\Cpp'
print('總列數：{0}，不重複列數：{1}'.format(code_num, len(NotRepeatedLines)))
print('檔案數量：{0}'.format(file_num))

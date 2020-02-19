fp = open('sample.txt')
print(fp.read(4))	#從目前位置讀取前4個字元
print(fp.read(18))	#英文字和中文字一樣對待
print(fp.read())	#從目前位置讀取後面的所有內容
fp.close()			#關閉檔案物件

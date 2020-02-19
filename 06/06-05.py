with open('data.txt', 'r') as fp:
    data = fp.readlines()				#讀取所有行
data = [line.strip() for line in data]	#刪除每行兩側的空白字元
data = ','.join(data)				#合併所有行
data = data.split(',')				#分割得到所有數字
data = [int(item) for item in data]	#轉換為數字
data.sort()							#昇冪排序
data = ','.join(map(str,data))		#將結果轉換為字串
with open('data_asc.txt', 'w') as fp:	#將結果寫入檔案
    fp.write(data)

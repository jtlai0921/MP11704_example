import pickle

n = 7
i = 13000000
a = 99.056
s = '中國人民 123abc'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 10, 8)
coll = {4, 5, 6}
dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
f = open('sample_pickle.dat', 'wb')	#以寫入模式打開啟二進位檔案
try:
    pickle.dump(n, f)		#對象物件個數
    pickle.dump(i, f)		#寫入整數
    pickle.dump(a, f)		#寫入實數
    pickle.dump(s, f)		#寫入字串
    pickle.dump(lst, f)		#寫入列表
    pickle.dump(tu, f)		#寫入元組
    pickle.dump(coll, f)		#寫入集合
    pickle.dump(dic, f)		#寫入字典
except:
    print('寫文件入檔案異常！')
finally:
    f.close()

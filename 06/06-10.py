import pickle

f = open('sample_pickle.dat', 'rb')
n = pickle.load(f)			#讀取檔案的資料個數
for i in range(n):
	x = pickle.load(f)
	print(x)
f.close()

import struct

n = 1300000000
x = 96.45
b = True
s = 'a1@中國'
sn = struct.pack('if?', n, x, b)	#序列化，i表示整數，f表示實數，?表示邏輯值
f = open('sample_struct.dat', 'wb')
f.write(sn)
f.write(s.encode())				#字串需要編碼為位元組，再寫入檔案
f.close()

import struct

f = open('sample_struct.dat', 'rb')
sn = f.read(9)
tu = struct.unpack('if?', sn)		#以指定的格式反序列化
print(tu)
n, x, b1 = tu
print('n=',n, 'x=',x, 'b1=',b1)
s = f.read(9)
s = s.decode()					#解碼字串
print('s=', s)

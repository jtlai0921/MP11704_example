import math

n = input("Input an integer:")
n = int(n)
m = int(math.sqrt(n)+2)
for i in range(2, m):
	if n%i == 0:
		print('No')
		break
else:
	print('Yes')

import socket
import uuid

ip = socket.gethostbyname(socket.gethostname())	#本機IP地址
node = uuid.getnode()
macHex = uuid.UUID(int=node).hex[-12:]
mac = []
for i in range(len(macHex))[::2]:
    mac.append(macHex[i:i+2])
mac = ':'.join(mac)							#網卡實體位址
print('IP:', ip)
print('MAC:', mac)

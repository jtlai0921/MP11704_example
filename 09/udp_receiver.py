import socket
#使用IPV4協定，以UDP協定傳輸資料
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#繫結連接埠和埠號，空字串表示本機任何可用的IP位址
s.bind(('', 5000))
while True:
    data, addr = s.recvfrom(1024)
    #顯示接收的內容
    print('received message:{0} from PORT {1} on {2}'.format(data.decode(),
                                                     addr[1], addr[0]))
    if data.decode().lower() == 'bye':
        break
s.close( )

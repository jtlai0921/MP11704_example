import socket

#伺服端主機IP位址和連接埠號
HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #連接伺服器
    s.connect((HOST, PORT))
except Exception as e:
    print('Server not found or not open')
    sys.exit()
while True:
    c = input('Input the content you want to send:')
    #傳送資料
    s.sendall(c.encode())
    #從伺服端接收資料
    data = s.recv(1024)
    data = data.decode()
    print('Received:', data)
    if c.lower() == 'bye':
        break
#關閉連接
s.close()

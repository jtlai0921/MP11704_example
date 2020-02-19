import socket

words = {'how are you?':'Fine,thank you.', 'how old are you?':'38',
        'what is your name?':'Dong FuGuo', "what's your name?":'Dong FuGuo',
        'where do you work?':'SDIBT', 'bye':'Bye'}
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#繫結socket
s.bind((HOST, PORT))
#開始監聽用戶端連接
s.listen(1)
print('Listening at port:',PORT)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('Received message:', data)
    conn.sendall(words.get(data, 'Nothing').encode())
conn.close()
s.close()

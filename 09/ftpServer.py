import socket
import threading
import os
import struct

#使用者帳號、密碼、主目錄
#也可以把這些資料存放到資料庫
users = {'zhangsan':{'pwd':'zhangsan1234', 'home':r'c:\python 3.5'},
         'lisi':{'pwd':'lisi567', 'home':'c:\\'}}

def server(conn,addr, home):
    print('新用戶端：'+str(addr))
    #進入目前帳號主目錄
    os.chdir(home)
    while True:
        data = conn.recv(100).decode().lower()
        #顯示用戶端輸入的每一道命令
        print(data)
        #用戶端退出
        if data in ('quit', 'q'):
            break
        #查看目前資料夾的檔案列表
        elif data in ('list', 'ls', 'dir'):
            files = str(os.listdir(os.getcwd()))
            files = files.encode()
            #先傳送位元組字串大小，再傳送位元組字串
            conn.send(struct.pack('I', len(files)))
            conn.send(files)
        #切換至上一層目錄
        elif ''.join(data.split()) == 'cd..':
            cwd = os.getcwd()
            newCwd = cwd[:cwd.rindex('\\')]
            #考慮根目錄的情況
            if newCwd[-1] == ':':
                newCwd += '\\'
            #限定使用者主目錄
            if newCwd.lower().startswith(home):
                os.chdir(newCwd)
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #查看目前的目錄
        elif data in ('cwd', 'cd'):
            conn.send(str(os.getcwd()).encode())
        elif data.startswith('cd '):
            #指定最大分隔次數，考慮目的資料夾帶有空格的情況
            #只允許以相對路徑進行跳轉
            data = data.split(maxsplit=1)
            if len(data) == 2 and  os.path.isdir(data[1]) \
               and data[1]!=os.path.abspath(data[1]):
                os.chdir(data[1])
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #下載檔案
        elif data.startswith('get '):
            data = data.split(maxsplit=1)
            #檢查檔案是否存在
            if len(data) == 2 and os.path.isfile(data[1]):
                conn.send(b'ok')
                fp = open(data[1], 'rb')
                while True:
                    content = fp.read(4096)
                    #傳送檔案結束
                    if not content:
                        conn.send(b'overxxxx')
                        break
                    #傳送檔案內容
                    conn.send(content)
                    if conn.recv(10) == b'ok':
                        continue
                fp.close()
            else:
                conn.send(b'no')
        #無效命令
        else:
            pass
            
    conn.close()
    print(str(addr)+'關閉連接')

#建立Socket，監聽本地連接埠，並等待用戶端連接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10600))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    #驗證用戶端輸入的帳號和密碼是否正確
    userId, userPwd = conn.recv(1024).decode().split(',')
    if userId in users and users[userId]['pwd'] == userPwd:
        conn.send(b'ok')
        #為每個用戶端連接建立與啟動一個執行緒
        #參數為連接、用戶端位址、帳號主目錄
        home = users[userId]['home']
        t = threading.Thread(target=server, args=(conn,addr,home))
        t.daemon = True
        t.start()
    else:
        conn.send(b'error')

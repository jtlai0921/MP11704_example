import socket
import sys
import re
import struct
import getpass

def main(serverIP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP, 10600))
    userId = input('請輸入帳號名稱：')
    #以getpass模組的getpass()方法取得密碼，不顯示
    userPwd = getpass.getpass('請輸入密碼：')
    message = userId+','+userPwd
    sock.send(message.encode())
    login = sock.recv(100)
    #驗證是否登錄成功
    if login == b'error':
        print('帳號名稱或密碼錯誤')
        return
    #整數編碼大小
    intSize = struct.calcsize('I')
    while True:
        #接收用戶端命令，其中##>是提示符號
        command = input('##> ').lower().strip()
        #未輸入任何有效字元，提前進入下一次迴圈，等待使用者繼續輸入
        if not command:
            continue
        #向伺服端傳送命令
        command = ' '.join(command.split())
        sock.send(command.encode())
        #退出
        if command in ('quit', 'q'):
            break
        #查看檔案列表
        elif command in ('list', 'ls', 'dir'):
            #先接收位元組字串大小，再根據情況接收適當數量的位元組字串
            loc_size = struct.unpack('I', sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        #切換至上一層目錄
        elif ''.join(command.split()) == 'cd..':
            print(sock.recv(100).decode())
        #查看目前工作目錄
        elif command in ('cwd', 'cd'):
            print(sock.recv(1024).decode())
        #切換至子資料夾
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
        #從伺服器下載檔案
        elif command.startswith('get '):
            isFileExist = sock.recv(20)
            #檔案不存在
            if isFileExist != b'ok':
                print('error')
            #檔案存在，開始下載
            else:
                print('downloading.', end='')
                fp = open(command.split()[1], 'wb')
                while True:
                    #顯示進度
                    print('.', end='')
                    data = sock.recv(4096)
                    if data == b'overxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
                
        #無效命令
        else:
            print('無效命令')
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
    serverIP = sys.argv[1]
    #以規則運算式判斷伺服器位址是否為合法的IP位址
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', serverIP):
        main(serverIP)
    else:
        print('伺服器位址不合法')
        exit()

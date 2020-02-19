import sys
import socket
import threading

def middle(conn, addr):
    #面對伺服器的Socket
    sockDst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockDst.connect((ipServer,portServer))
    while True:
        data = conn.recv(1024).decode()
        print('收到用戶端訊息：'+data)
        if data == '不要發給伺服器':
            conn.send('該訊息已被代理伺服器過濾'.encode())
            print('該訊息已過濾')
        elif data.lower() == 'bye':
            print(str(addr)+'用戶端關閉連接')
            break
        else:
            sockDst.send(data.encode())
            print('已轉發伺服器')
            data_fromServer = sockDst.recv(1024).decode()
            print('收到伺服器回覆的訊息：'+data_fromServer)
            if data_fromServer == '不要發給用戶端':
                conn.send('該訊息已被代理伺服器修改'.encode())
                print('訊息已被篡改')
            else:
                conn.send(b'Server reply:'+data_fromServer.encode())
                print('已轉發伺服器訊息給用戶端')
        
    conn.close()
    sockDst.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('', portScr))
    sockScr.listen(200)
    print('代理已啟動')
    while True:
        try:
            conn, addr = sockScr.accept()
            t = threading.Thread(target=middle, args=(conn, addr))
            t.start()
            print('新客戶：'+str(addr))
        except:
            pass
        
if __name__ == '__main__':
    try:
        #(本機IP地址,portScr)<==>(ipServer,portServer)
        #代理伺服器監聽連接埠
        portScr = int(sys.argv[1])
        #伺服器IP位址與連接埠號
        ipServer = sys.argv[2]
        portServer = int(sys.argv[3])
        main()
    except:
        print('Sth error')

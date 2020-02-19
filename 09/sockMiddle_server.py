import sys
import socket
import threading

#回覆訊息，原樣返回
def replyMessage(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data)
        if data.decode().lower() == 'bye':
            break
    conn.close()

def main():
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('', port))
    sockScr.listen(200)
    while True:
        try:
            conn, addr = sockScr.accept()
            #只允許特定主機存取本伺服器
            if addr[0] != onlyYou:
                conn.close()
                continue
            #建立並啟動執行緒
            t = threading.Thread(target=replyMessage, args=(conn,))
            t.start()        
        except:
            print('error')

if __name__ == '__main__':
    try:
        #取得命令列參數，port為伺服器監聽連接埠
        #只允許IP位址為onlyYou的主機存取
        port = int(sys.argv[1])
        onlyYou = sys.argv[2]
        main()
    except:
        print('Must give me a number as port')

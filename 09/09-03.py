import socket
import threading
import time

activeDegree = dict()
flag = 1
def main():
    global activeDegree
    global flag
    #取得本機IP地址
    HOST = socket.gethostbyname(socket.gethostname())
    #建立原始通訊端，適用Windows平台
    #對於其他作業系統，要把socket.IPPROTO_IP替換為socket.IPPROTO_ICMP
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    #設定在捕獲的封包中含有IP標頭
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    #啟用混合模式，捕捉所有封包
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    #開始捕捉封包
    while flag:
        c = s.recvfrom(65565)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host, 0)+1
        #假設本機IP位址為10.2.1.8
        if c[1][0]!='10.93.2.31': 
            print(c)
    #關閉混合模式
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)

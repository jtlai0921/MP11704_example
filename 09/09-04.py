import socket
import multiprocessing

def ports(ports_service):
    #取得常用連接埠對應的服務名稱
    for port in list(range(1,100))+[143, 145, 113, 443, 445, 3389, 8080, 521, 5000]:
        try:
            ports_service[port] = socket.getservbyport(port)
        except socket.error:
            pass

def ports_scan(host, ports_service):
    ports_open = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #逾時時間的不同，將影響掃描結果的精確度
        sock.settimeout(0.01)
    except socket.error:
        print('socket creation error')
        sys.exit()
    for port in ports_service:
        try:
            #嘗試連結指定連接埠
            sock.connect((host,port))
            #記錄開啟的連接埠
            ports_open.append(port)
            sock.close()
        except socket.error:
            pass
    return ports_open

if __name__=='__main__':
    m = multiprocessing.Manager()
    ports_service = dict()
    results = dict()
    ports(ports_service)
    #建立處理程序池，允許最多8個處理程序同時執行
    pool = multiprocessing.Pool(processes=8)
    net = '10.9.1.'
    for host_number in map(str, range(80,83)):
        host = net+host_number
        #建立一個新的處理程序，同時記錄執行結果
        results[host] = pool.apply_async(ports_scan, (host, ports_service))
        print('starting '+host+'...')
    #關閉處理程序池，close()必須在join()之前執行
    pool.close()
    #等待池中的處理程序全部執行結束
    pool.join()

    #列印輸出結果
    for host in results:
        print('='*30)
        print(host,'.'*10)
        for port in results[host].get():
            print(port, ':', ports_service[port])

from time import sleep
from socket import gethostbyname
from datetime import datetime

def get_ipAddresses(url):
    ipAddresses = [0]
    while True:
        sleep(0.5)				#暫停0.5秒
        ip = gethostbyname(url)
        if ip != ipAddresses[-1]:	#目標主機IP位址發生變化
            ipAddresses.append(ip)
            print(str(datetime.now())[:19]+'===>'+ip)
get_ipAddresses(r'www.microsoft.com')

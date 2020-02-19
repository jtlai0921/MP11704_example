import socket
import nmap

nmScan = nmap.PortScanner()			#建立連接埠掃描物件
ip = socket.gethostbyname('www.microsort.com')	#取得目標主機的IP位址
nmScan.scan(ip,'80')				#掃描指定連接埠
print(nmScan[ip]['tcp'][80]['state'])	#查看連接埠狀態

import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#假設192.168.0.103是接收端機器的IP位址
s.sendto(sys.argv[1].encode() , ("10.93.2.31" ,5000))
s.close( )

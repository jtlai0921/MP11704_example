import socket
import struct
from time import sleep
from PIL import ImageGrab

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #假設監控端主機IP位址為10.2.1.2，並監聽10600連接埠
        sock.connect(('10.2.1.2', 10600))
        #本地端全螢幕截圖
        im = ImageGrab.grab()
        size = im.size
        #本地端截圖轉換為位元組後進行傳送
        imageBytes = im.tobytes()
        #傳送的位元組總長度和圖形大小
        fhead=struct.pack('I128sI',len(imageBytes), str(size).encode(), 
                       len(str(size).encode()))
        sock.send(fhead)
        rest = len(imageBytes)
        bufferSize = 1024*10
        while True:
            if rest > bufferSize:
                temp = imageBytes[:bufferSize]
                imageBytes = imageBytes[bufferSize:]
            else:
                temp = imageBytes[:]
            sock.send(temp)
            rest = rest - len(temp)            
            #本次截圖傳送完成
            if rest == 0:
                if sock.recv(100) == b'ok':
                    print('ok')
                    break
        sock.close()
    except:
        print('無法連接監控端')

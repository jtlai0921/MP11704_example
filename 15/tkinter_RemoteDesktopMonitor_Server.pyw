import tkinter
import socket
import time
import threading
import struct
from PIL import Image, ImageTk

def updateCanvas(canvas):
    global imageId
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 10600))
    sock.listen(1)
    while running.get() == 1:
        #自我調整目前監控視窗的大小
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        conn, addr = sock.accept()
        tempImageBytes = b''
        #圖形位元組數量
        len_head = struct.calcsize('I128sI')
        data = conn.recv(len_head)
        length, size ,sizeLength= struct.unpack('I128sI',data)
        length = int(length)
        rest = length
        bufferSize = 1024*10
        size = eval(size[:int(sizeLength)])
        while running.get() == 1:
            if rest > bufferSize:
                data = conn.recv(1024*10)
            else:
                data = conn.recv(rest)
            tempImageBytes += data
            rest = rest - len(data)
            
            #遠端桌面截圖接收完成，顯示圖形
            if rest == 0:
                tempImage = Image.frombytes('RGB', size, tempImageBytes)
                tempImage = tempImage.resize((width,height))
                #tempImage.save('temp.png')
                tempImage = ImageTk.PhotoImage(tempImage)
                #清除上一張截圖
                try:
                    canvas.delete(imageId)
                except:
                    pass
                imageId = canvas.create_image(width//2, height//2, image=tempImage)
                #canvas.update()
                #通知用戶端可以發送下一張截圖
                conn.send(b'ok')
                print('ok')
                break
            
        conn.close()

root = tkinter.Tk()
#主程序視窗位置和大小
root.geometry('640x480+400+300')
width = 640
height = 480
root.title('遠端桌面監看系統v1.0---董付國')

#表示監控軟體是否運行的變數
running = tkinter.IntVar(root, 1)

#關閉監控視窗時觸發的訊息處理函數
def closeWindow():
    running.set(0)
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#使用子執行緒刷新監控視窗
t = threading.Thread(target=updateCanvas, args=(canvas,))
#關閉主執行緒時，強制關閉刷新視窗的子執行緒
t.daemon = True
t.start()
root.mainloop()

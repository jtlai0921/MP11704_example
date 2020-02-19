import tkinter
import threading
import datetime
import time

app = tkinter.Tk()
#不顯示標題列
app.overrideredirect(True)
#半透明表單
app.attributes('-alpha', 0.9)
#視窗總是在頂端顯示
app.attributes('-topmost', 1)
#設定初始大小與位置
app.geometry('110x25+100+100')
labelDateTime = tkinter.Label(app)
labelDateTime.pack(fill=tkinter.BOTH, expand=tkinter.YES)
labelDateTime.configure(bg = 'gray')
#變數X和Y用來記錄滑鼠左鍵按下的位置
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
#表示視窗是否可拖動的變數
canMove = tkinter.IntVar(value=0)
#表示是否仍在執行的變數
still = tkinter.IntVar(value=1)

def onLeftButtonDown(event):
    #開始拖動時增加透明度
    app.attributes('-alpha', 0.4)
    #按滑鼠左鍵後，記錄目前位置
    X.set(event.x)
    Y.set(event.y)
    #標記視窗可拖動
    canMove.set(1)
#繫結滑鼠左鍵按一下事件處理函數
labelDateTime.bind('<Button-1>', onLeftButtonDown)

def onLeftButtonUp(event):
    #停止拖動時，恢復透明度
    app.attributes('-alpha', 0.9)
    #釋放滑鼠左鍵，標記視窗不可拖動
    canMove.set(0)
#繫結滑鼠左鍵釋放事件處理函數
labelDateTime.bind('<ButtonRelease-1>', onLeftButtonUp)

def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    #重新計算與修改視窗的新位置
    newX = app.winfo_x()+(event.x-X.get())
    newY = app.winfo_y()+(event.y-Y.get())
    g = '110x25+'+str(newX)+'+'+str(newY)
    app.geometry(g)
#繫結滑鼠左鍵移動事件處理函數
labelDateTime.bind('<B1-Motion>', onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    t.join(0.2)
    #關閉視窗
    app.destroy()
#繫結按滑鼠右鍵事件處理函數
labelDateTime.bind('<Button-3>', onRightButtonDown)
#顯示目前時間的函數
def nowDateTime():
    while still.get()==1:
        now = datetime.datetime.now()
        s = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '
        s = s+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        #顯示目前時間
        labelDateTime['text'] = s
        time.sleep(0.2)
#建立執行緒
t = threading.Thread(target=nowDateTime)
t.daemon = True
t.start()

app.mainloop()

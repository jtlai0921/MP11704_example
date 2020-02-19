import tkinter
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep

root = tkinter.Tk()
root.geometry('100x40+400+300')
root.resizable(False, False)


class MyCapture:
    def __init__(self, png):
        #變數X和Y用來記錄按下滑鼠左鍵的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        #螢幕尺寸
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        #建立頂端元件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        #不顯示最大化、最小化按鈕
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth,
                         height=screenHeight)
        #顯示全螢幕截圖，在其上進行區域截圖
        self.image = tkinter.PhotoImage(file=png)
        self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)
        #按下滑鼠左鍵的位置
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            #開始截圖
            self.sel = True
        self.canvas.bind('<Button-1>', onLeftButtonDown)
        #移動滑鼠左鍵，顯示選取的區域
        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                #刪除剛畫完的圖形，不然移動滑鼠時是黑壓壓的一片矩形
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            lastDraw = self.canvas.create_rectangle(self.X.get(),
                         self.Y.get(), event.x, event.y, outline='black')
        self.canvas.bind('<B1-Motion>', onLeftButtonMove)
        #取得釋放滑鼠左鍵的位置，保存區域截圖
        def onLeftButtonUp(event):
            self.sel = False
            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            sleep(0.1)
            #考慮滑鼠左鍵從右下方按下、而從左上方釋放的截圖
            left, right = sorted([self.X.get(), event.x])
            top, bottom = sorted([self.Y.get(), event.y])
            pic = ImageGrab.grab((left+1, top+1, right, bottom))
            #彈出儲存截圖對話方塊
            fileName = tkinter.filedialog.asksaveasfilename(title='儲存截圖', filetypes=[('image', '*.jpg *.png')])
            if fileName:
                pic.save(fileName)
            #關閉目前視窗
            self.top.destroy()
        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    #開始截圖
def buttonCaptureClick():
    #最小化主視窗
    root.state('icon')
    sleep(0.2)
    
    filename = 'temp.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    #顯示全螢幕截圖
    w = MyCapture(filename)
    buttonCapture.wait_window(w.top)
    #截圖結束，恢復主視窗，並刪除臨時的全螢幕截圖檔
    root.state('normal')
    os.remove(filename)
buttonCapture = tkinter.Button(root, text='截圖', command=buttonCaptureClick)
buttonCapture.place(x=10, y=10, width=80, height=20)
#啟動主迴圈
root.mainloop()

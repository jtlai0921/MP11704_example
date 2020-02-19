import tkinter
import tkinter.messagebox

#自訂視窗類別
class myWindow:
    #構造函數
    def __init__(self, root, myTitle, flag):
        #建立視窗
        self.top = tkinter.Toplevel(root, width=300, height=200)
        #設定視窗標題
        self.top.title(myTitle)
        #設定頂端顯示
        self.top.attributes('-topmost', 1)
        #根據不同情況在視窗置放不同的元件
        if flag==1:
            label = tkinter.Label(self.top, text=myTitle)
            label.place(x=50, y=50)
        elif flag==2:
            def buttonOK():
                #彈出訊息提示框
                tkinter.messagebox.showinfo(title='Python V5', message='I am Alvin Liao')
            button = tkinter.Button(self.top, text=myTitle, command=buttonOK)
            button.place(x=50, y=50)
#建立應用程式主視窗
root = tkinter.Tk()
#設定主視窗大小
root.config(width=400)
root.config(height=200)
#設定主視窗標題
root.title('Multiple Windows Demo------Dong Fuguo')
window1 = tkinter.IntVar(root, value=0)
window2 = tkinter.IntVar(root, value=0)
#按一下按鈕1，建立並彈出新視窗
def buttonClick1():
    if window1.get()==0:
        window1.set(1)
        w1 = myWindow(root, 'First Window', 1)
        button1.wait_window(w1.top)
        window1.set(0)
button1 = tkinter.Button(root, text='First Window', command=buttonClick1)
button1.place(x=70, y=40, height=40, width=200)

def buttonClick2():
    if window2.get()==0:
        window2.set(1)
        w1 = myWindow(root, 'Second Window', 2)
        button2.wait_window(w1.top)
        window2.set(0)
button2 = tkinter.Button(root, text='Second Window', command=buttonClick2)
button2.place(x=70, y=100, height=40, width=200)
#啟動主迴圈
root.mainloop()

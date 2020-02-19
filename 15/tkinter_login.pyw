import tkinter
import tkinter.messagebox

#建立應用程式視窗
root = tkinter.Tk()
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')
#建立標籤
labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, width=80)
#將標籤置於視窗上
labelName.place(x=10, y=5, width=80, height=20)
#建立文字方塊，同時設定關聯的變數
entryName = tkinter.Entry(root, width=80,textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root, text='User Pwd:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)
#建立密碼文字方塊
entryPwd = tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)
#登錄按鈕事件處理函數
def login():
    #取得使用者帳號和密碼
    name = entryName.get()
    pwd = entryPwd.get()
    if name=='admin' and pwd=='123456':
        tkinter.messagebox.showinfo(title='Python tkinter',message='OK')
    else:
        tkinter.messagebox.showerror('Python tkinter', message='Error')
#建立按鈕元件，同時設定按鈕事件處理函數
buttonOk = tkinter.Button(root, text='Login', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)
#取消按鈕事件處理函數
def cancel():
    #清空使用者輸入的帳號和密碼
    varName.set('')
    varPwd.set('')
buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

#啟動訊息迴圈
root.mainloop()

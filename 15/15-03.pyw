import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext

#建立應用程式視窗
app = tkinter.Tk()
app.title('My Notepad----by Dong Fuguo')
app['width'] = 800
app['height'] = 600

textChanged = tkinter.IntVar(value=0)
#目前檔案名稱
filename = ''

#建立選單
menu = tkinter.Menu(app)
#File選單
submenu = tkinter.Menu(menu, tearoff=0)
def Open():
    global filename
    #如果內容已改變，先儲存
    if textChanged.get():
        yesno = tkinter.messagebox.askyesno(title='Save or not?',
                  message='Do you want to save?')
        if yesno == tkinter.YES:
            Save()
    filename = tkinter.filedialog.askopenfilename(title='Open file',
                 filetypes=[('Text files', '*.txt')])
    if filename:
        #清空內容,0.0是lineNumber.Column的表示方法
        txtContent.delete(0.0, tkinter.END)
        fp = open(filename, 'r')
        txtContent.insert(tkinter.INSERT, ''.join(fp.readlines()))
        fp.close()
        #標記為尚未修改
        textChanged.set(0)
#建立Open功能表，並繫結功能表事件處理函數
submenu.add_command(label='Open', command=Open)

def Save():
    global filename
    #如果是第一次儲存檔案，則開啟「另存新檔」視窗
    if not filename:
        SaveAs()
    #如果內容發生改變，便儲存
    elif textChanged.get():
        fp = open(filename, 'w')
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        textChanged.set(0)
submenu.add_command(label='Save', command=Save)

def SaveAs():
    global filename
    #開啟「另存新檔」視窗
    newfilename = tkinter.filedialog.asksaveasfilename(title='Save As',
                     initialdir=r'c:\\', initialfile='new.txt')
    #如果指定檔名，則儲存檔案
    if newfilename:
        fp = open(newfilename, 'w')
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        filename = newfilename
        textChanged.set(0)
submenu.add_command(label='Save As', command=SaveAs)
#加上分隔線
submenu.add_separator()
def Close():
    global filename
    Save()
    txtContent.delete(0.0, tkinter.END)
    #清空檔案名稱
    filename = ''
submenu.add_command(label='Close', command=Close)
#將子功能表關聯到主選單
menu.add_cascade(label='File', menu=submenu)

#Edit選單
submenu = tkinter.Menu(menu, tearoff=0)
#復原最後一次操作
def Undo():
    #啟用undo標誌
    txtContent['undo'] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass
submenu.add_command(label='Undo', command=Undo)

def Redo():
    txtContent['undo'] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass
submenu.add_command(label='Redo', command=Redo)
submenu.add_separator()

def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())
submenu.add_command(label='Copy', command=Copy)

def Cut():
    Copy()
    #刪除所選內容
    txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
submenu.add_command(label='Cut', command=Cut)

def Paste():
    #如果沒有選中內容，則直接貼到滑鼠位置
    #如果有選中內容，則先刪除再貼上
    try:
        txtContent.insert(tkinter.SEL_FIRST, txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        #如果貼上成功就結束本函數，以免異常處理結構執行完成之後再次貼上
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT, txtContent.clipboard_get())    
submenu.add_command(label='Paste', command=Paste)
submenu.add_separator()

def Search():
    #取得要尋找的內容
    textToSearch = tkinter.simpledialog.askstring(title='Search',
                      prompt='What to search?')
    start = txtContent.search(textToSearch, 0.0, tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title='Found', message='Ok')
submenu.add_command(label='Search', command=Search)
menu.add_cascade(label='Edit', menu=submenu)

#Help選單
submenu = tkinter.Menu(menu, tearoff=0)
def About():
    tkinter.messagebox.showinfo(title='About', message='Author:Dong Fuguo')
submenu.add_command(label='About', command=About)
menu.add_cascade(label='Help', menu=submenu)
#將建立的功能表關聯到應用程式視窗
app.config(menu=menu)

#建立文字編輯元件，並自動適應視窗大小
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>', KeyPress)

app.mainloop()

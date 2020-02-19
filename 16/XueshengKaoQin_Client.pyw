import tkinter
import tkinter.ttk
import tkinter.scrolledtext
import tkinter.messagebox
import tkinter.filedialog
import socket
import re
import os
import sys
import struct
import threading
import time
import ctypes

#先將pip升級到最新版本
path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install --upgrade pip'
os.system(path)
#匯入必要的擴展庫
try:
    import psutil
except:
    path = os.path.dirname(sys.executable)+'\\scripts\\pip install psutil'
    os.system(path)
    import psutil
try:
    from PIL import ImageGrab, Image, ImageTk
except:
    path = os.path.dirname(sys.executable)+'\\scripts\\pip install pillow'
    os.system(path)
    from PIL import ImageGrab, Image, ImageTk

root = tkinter.Tk(screenName='User login')        #建立應用程式視窗
root.title('課堂管理系統客戶端-董付國')
root.geometry('320x150+500+300')
root.resizable(False, False)   #不允許改變視窗大小

def closeWindow():
    tkinter.messagebox.showerror(title='警告',
                                 message='不許關閉，好好學習！')
    return
##    #結束搜索伺服器
##    if int_searchServer.get() == 1:
##        int_searchServer.set(0)
##    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)
###退出程式時執行上面的函數
##import atexit
##atexit.register(closeWindow)

xuehao = tkinter.StringVar(root)
xuehao.set('')
xingming = tkinter.StringVar(root)
xingming.set('')
server_IP = tkinter.StringVar(root)
server_IP.set('10.93.2.31')  #預設伺服器位址

labelXuehao = tkinter.Label(root, text='學號：', #建立標籤
                          justify=tkinter.RIGHT,
                          width=80)
labelXuehao.place(x=10, y=5, width=80, height=20)    #將標籤放到視窗上

entryXuehao = tkinter.Entry(root, width=150,         #建立文字框
                          textvariable=xuehao)    #同時設定相關的變數
entryXuehao.place(x=100, y=5, width=150, height=20)

labelXingming = tkinter.Label(root, text='姓名：', justify=tkinter.RIGHT, width=80)
labelXingming.place(x=10, y=30, width=80, height=20)

entryXingming = tkinter.Entry(root, width=150,
                         textvariable=xingming)
entryXingming.place(x=100, y=30, width=150, height=20)

labelServerIP = tkinter.Label(root, text='伺服器IP位址：', justify=tkinter.RIGHT, width=80)
labelServerIP.place(x=10, y=60, width=80, height=20)
entryServerIP = tkinter.Entry(root, width=150, textvariable=server_IP)
entryServerIP.place(x=100, y=60, width=150, height=20)

# 自動登入
try:
    path = os.getenv('temp')
    filename = path + '\\' + 'info.txt'
    with open(filename) as fp:
        xuehao1, xingming1, ip1 = fp.read().strip().split(',')
    xuehao.set(xuehao1)
    xingming.set(xingming1)
    server_IP.set(ip1)
except:
    pass

int_searchServer = tkinter.IntVar(root, value=1)
#每3秒鐘接收一次伺服器廣播訊息，修改伺服器IP位址
def findServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)               #建立socket物件
    sock.bind(('', 5000))                                                 #繫結socket
    try:
        while int_searchServer.get() == 1:
            data, addr = sock.recvfrom(1024)                              #接收訊息
            if data.decode() == 'ServerIP':                               #輸出收到的訊息
                server_IP.set(addr[0])
            time.sleep(3)
    except:
        pass
thread_findServer = threading.Thread(target=findServer)
thread_findServer.start()

def buttonOKClick():                #登入按鈕事件處理函數
    xuehao = entryXuehao.get()      #抓取學號
    xingming = entryXingming.get()  #抓取姓名
    serverIP = entryServerIP.get()
    if not re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 30300))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不是點名時間！')
        return
    
    #抓取客戶端MAC位址，使用MAC+IP保證每台電腦每節課只能點名一次
    import uuid
    node = uuid.getnode()
    macHex = uuid.UUID(int=node).hex[-12:]
    mac = []
    for i in range(len(macHex))[::2]:
        mac.append(macHex[i:i+2])
    mac = ''.join(mac)
        
    sock.sendall(','.join((xuehao,xingming,mac)).encode())
    
    data = sock.recv(1024).decode()
    if data.lower() == 'ok':
        #點名成功
        sock.close()

        #儲存學號、姓名和伺服器IP位址，方便下次自動填寫資料
        path = os.getenv('temp')
        filename = path + '\\' + 'info.txt'
        with open(filename, 'w') as fp:
            fp.write(','.join((xuehao, xingming, serverIP)))
        
        tkinter.messagebox.showinfo('恭喜', xuehao + ',' + xingming + '  報到點名成功')
        return
    elif data.lower() == 'repeat':
        sock.close()
        tkinter.messagebox.showerror('很抱歉', '不允許重複報到！')
        return
    elif data.lower() == 'notmatch':
        sock.close()
        tkinter.messagebox.showerror('很抱歉', '學號與姓名不符合！')
        return
    elif data.lower() == 'daidianming':
        sock.close()
        tkinter.messagebox.showerror('很抱歉', '不允許替別人點名，警告一次！')
        return
buttonOk = tkinter.Button(root, text='報到',      #建立按鈕元件
                          command=buttonOKClick)  #同時設定按鈕事件處理函數
buttonOk.place(x=30, y=90, width=80, height=20)

def buttonZuoyeClick():
    xuehao = entryXuehao.get()  	#抓取帳號
    xingming = entryXingming.get()  #抓取密碼
    serverIP = entryServerIP.get()
    if not re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 30100))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不是交作業時間！')
        return
    
    filename = xuehao+'_'+xingming+'.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    
    BUFSIZE = 1024
    FILEINFO_SIZE=struct.calcsize('I128sI')    
    
    #開始傳送截圖
    fhead=struct.pack('I128sI',len(filename),filename.encode(),os.stat(filename).st_size)
    sock.send(fhead)		#傳送檔名和大小等資訊
    data = sock.recv(1024)	#接收伺服器回應
    data = data.decode()
    if data.lower() == 'notmatch':
        tkinter.messagebox.showerror('很抱歉', '學號與姓名不符合！')
        sock.close()
        return
        
    fp = open(filename,'rb')
    while True:
        filedata = fp.read(BUFSIZE)
        if not filedata:
            break
        sock.send(filedata)
    fp.close()
    sock.close()
    tkinter.messagebox.showinfo('恭喜', '交作業成功')
buttonZuoye = tkinter.Button(root, text='全螢幕截圖交作業', command=buttonZuoyeClick)
buttonZuoye.place(x=120, y=90, width=100, height=20)

#提問功能模組
int_windowTiwen = tkinter.IntVar(root, value=0)
string_wenti = tkinter.StringVar(root, value='')
class windowTiwen:
    def __init__(self, root):
        #建立面板容器，用來擺放其他元件
        self.top = tkinter.Toplevel(root, width=300, height=180)
        self.top.title('請輸入你的問題')
        self.top.attributes('-topmost', 1)
        entryMessage = tkinter.scrolledtext.ScrolledText(self.top, wrap=tkinter.WORD)#問題內容
        entryMessage.place(x=10, y=20, width=280, height=100)
        def buttonTiwenClick():
            #回覆，解答
            wenti = entryMessage.get(0.0, tkinter.END)
            wenti = wenti.strip()
            string_wenti.set(wenti)            
            self.top.destroy()
        buttonTiwen = tkinter.Button(self.top, text='確定提問', command=buttonTiwenClick)
        buttonTiwen.place(x=80, y=130, width=80, height=20)
def buttonTiwenClick():
    if int_windowTiwen.get()==1:
        return
    
    xuehao = entryXuehao.get()  	#抓取帳號
    xingming = entryXingming.get()  #抓取密碼
    serverIP = entryServerIP.get()
    if not re.match('^(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}$', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 20000))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不允許提問！')
        return
    int_windowTiwen.set(1)
    w = windowTiwen(root)
    buttonTiwen.wait_window(w.top)
    int_windowTiwen.set(0)
    if string_wenti.get()!='':
        #如果確實有問題，則向伺服端傳送
        message = xuehao+','+xingming+':'+string_wenti.get()
        sock.sendall(message.encode())
        data = sock.recv(1024)
        data = data.decode()
        data = data.strip()
        if data.lower() == 'notmatch':
            tkinter.messagebox.showerror('很抱歉', '學號與姓名不相符！')
            sock.close()
            return
        elif data.lower() == 'wait':
            tkinter.messagebox.showinfo('請稍等', '該問題稍後會統一進行講解！')
            sock.close()
            return
        else:
            tkinter.messagebox.showinfo('老師回覆', data)
            sock.close()
            return
buttonTiwen = tkinter.Button(root, text='提問', command=buttonTiwenClick)
buttonTiwen.place(x=230, y=90, width=40, height=20)

#自我測驗模組
int_windowZice = tkinter.IntVar(root, value=0)
class windowZice:
    def __init__(self, root, conn, xuehaoxingming):
        #建立面板容器，用來擺放其他元件
        self.top = tkinter.Toplevel(root, width=300, height=180)
        self.top.title('學生自測---'+xuehaoxingming)
        self.top.attributes('-topmost', 1)
        self.top.resizable(False, False) #不允許最大化
        def closeWindow():
            if int_windowZice.get() == 1:
                int_windowZice.set(0)
                conn.sendall('xxxx'.encode())
                conn.close()
            self.top.destroy()
        self.top.protocol('WM_DELETE_WINDOW', closeWindow)
        #從伺服器接收課程名稱清單，並以下拉式清單顯示
        data = conn.recv(1024)
        data = data.decode()
        kechengQingdan = data.split(',')
        labelKechengmingcheng = tkinter.Label(self.top, text='請選擇課程名稱：')
        labelKechengmingcheng.place(x=10, y=10, height=20, width=100)
        comboboxKechengmingcheng = tkinter.ttk.Combobox(self.top, values=kechengQingdan)
        comboboxKechengmingcheng.place(x=120, y=10, height=20, width=130)
        #每次改變課程名稱時，把self.currentID重新設為0
        def comboxboxKechengmingChanged(event):
            self.currentID = 0
        comboboxKechengmingcheng.bind('<<ComboboxSelected>>', comboxboxKechengmingChanged)

        #課程名稱
        string_Kecheng = tkinter.StringVar(self.top, value='')
        labelKecheng = tkinter.Label(self.top,text='', textvariable=string_Kecheng)
        labelKecheng.place(x=10, y= 40, height=20, width=100)
        #章節
        string_Zhangjie = tkinter.StringVar(self.top, value='')
        labelZhangjie = tkinter.Label(self.top, text='', textvariable=string_Zhangjie)
        labelZhangjie.place(x=130, y=40, height=20, width=80)

        #選擇題號下拉式清單
        tihao = [i for i in range(1,800)]
        comboTihao = tkinter.ttk.Combobox(self.top, values=tihao, width=50)
        comboTihao.place(x=220, y=40, height=20, width=50)
        def comboTihaoChanged(event):
            self.currentID = int(comboTihao.get())-1
            buttonNextClick()
        comboTihao.bind('<<ComboboxSelected>>', comboTihaoChanged)
        
        entryMessage = tkinter.scrolledtext.ScrolledText(self.top, wrap=tkinter.WORD)#問題內容
        entryMessage.place(x=10, y=70, width=280, height=70)
        self.currentID = 0
        def buttonPreClick():#上一題
            kechengmingchengSelected = comboboxKechengmingcheng.get()
            if not kechengmingchengSelected:
                tkinter.messagebox.showerror('很抱歉', '請選擇課程名稱！')
                return
            message = kechengmingchengSelected+'xx'+str(self.currentID)+'xxpre'
            conn.sendall(message.encode())
            data = conn.recv(1024)
            data = data.decode()
            if data == 'no':
                tkinter.messagebox.showerror('很抱歉', '沒有上一題了！')
                return
            kechengmingcheng, zhangjie, timu, self.daan, self.currentID = data.split('xx')
            entryMessage.delete(0.0, tkinter.END)		#刪除原來的題目內容
            entryMessage.insert(tkinter.INSERT, timu)	#顯示新題目內容
            string_Kecheng.set(kechengmingcheng)
            string_Zhangjie.set(zhangjie)
            #將題號選擇下拉式清單設定為目前題號
            comboTihao.set(self.currentID)
            
            
        buttonPre = tkinter.Button(self.top, text='上一題', command=buttonPreClick)
        buttonPre.place(x=40, y=150, width=60, height=20)
        def buttonNextClick():#下一題
            kechengmingchengSelected = comboboxKechengmingcheng.get()
            if not kechengmingchengSelected:
                tkinter.messagebox.showerror('很抱歉', '請選擇課程名稱！')
                return
            message = kechengmingchengSelected+'xx'+str(self.currentID)+'xxnext'
            conn.sendall(message.encode())
            data = conn.recv(1024)
            data = data.decode()
            if data == 'no':
                tkinter.messagebox.showerror('很抱歉', '沒有下一題了！')
                return
            kechengmingcheng, zhangjie, timu, self.daan, self.currentID = data.split('xx')
            entryMessage.delete(0.0, tkinter.END)		#刪除原來的題目內容
            entryMessage.insert(tkinter.INSERT, timu)	#顯示新題目內容
            string_Kecheng.set(kechengmingcheng)
            string_Zhangjie.set(zhangjie)
            #將題號下拉式清單設定為目前題號
            comboTihao.set(self.currentID)
        buttonNext = tkinter.Button(self.top, text='下一題', command=buttonNextClick)
        buttonNext.place(x=110, y=150, width=60, height=20)
        def buttonDaanClick():#查詢答案
            tkinter.messagebox.showinfo('本題答案', self.daan)
        buttonDaan = tkinter.Button(self.top, text='查詢答案', command=buttonDaanClick)
        buttonDaan.place(x=180, y=150, width=60, height=20)
        #預設開啟第一題
        buttonNextClick()
def buttonZiceClick():
    xuehao = entryXuehao.get()
    xingming = entryXingming.get()
    serverIP = entryServerIP.get()
    if not re.match('(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 10000))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不是自測時間！')
        return
    #向伺服端傳送學號和姓名
    sock.sendall((xuehao+','+xingming).encode())
    #開啟自測視窗
    int_windowZice.set(1)
    w = windowZice(root, sock, xuehao+','+xingming)
    buttonZice.wait_window(w.top)
    int_windowZice.set(0)
        
buttonZice = tkinter.Button(root, text='自我測驗', command=buttonZiceClick) 
buttonZice.place(x=30, y=120, width=80, height=20)

#上傳檔案交作業，伺服端應監聽10500連接埠
def buttonShangchuanWenjianJiaozuoyeClick():
    xuehao = entryXuehao.get()  	#抓取帳號
    xingming = entryXingming.get()  #抓取密碼
    serverIP = entryServerIP.get()
    if not re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 10500))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不是交作業時間！')
        return
    #檢查學生填寫的學號和姓名是否相符
    filename = tkinter.filedialog.askopenfilename(title='請選擇要上傳的Python程式或壓縮檔', filetypes=[('Python Files','*.py'), ('Python GUI Files','*.pyw'),('Rar files', '*.rar'), ('Zip files', '*.zip')])
    if filename:
        BUFSIZE = 1024
        FILEINFO_SIZE=struct.calcsize('I128sI')
        temp = xuehao+'_'+xingming+'_1_'+filename
        fhead=struct.pack('I128sI',len(temp),temp.encode(),os.stat(filename).st_size)
        sock.send(fhead)		#傳送檔名和大小等資訊
        data = sock.recv(1024)	#接收伺服器回應
        data = data.decode()
        if data.lower() == 'notmatch':
            tkinter.messagebox.showerror('很抱歉', '學號與姓名不符合！')
            sock.close()
            return
            
        fp = open(filename,'rb')
        while True:
            filedata = fp.read(BUFSIZE)
            if not filedata:
                break
            sock.send(filedata)
        fp.close()
        sock.close()
        tkinter.messagebox.showinfo('恭喜', '交作業成功！')
        
buttonShangchuanWenjianJiaozuoye = tkinter.Button(root, text='上傳檔案交作業', command=buttonShangchuanWenjianJiaozuoyeClick) 
buttonShangchuanWenjianJiaozuoye.place(x=120, y=120, width=100, height=20)

#線上考試模組
int_windowKaoshi = tkinter.IntVar(root, value=0)
class windowKaoshi:
    def __init__(self, root, conn, xuehaoxingming):
        #建立面板容器，用來擺放其他元件
        self.top = tkinter.Toplevel(root, width=300, height=220)
        self.top.title('線上考試---'+xuehaoxingming)
        self.top.attributes('-topmost', 1)
        self.top.resizable(False, False) #不允許最大化
        
        #關閉視窗事件
        def closeWindow():
            if int_windowZice.get() == 1:
                int_windowZice.set(0)
                conn.sendall('xxxx'.encode())
                conn.close()
                #結束禁用word，wps，記事本處理序的執行緒
                self.jinyong = False
            self.top.destroy()
        self.top.protocol('WM_DELETE_WINDOW', closeWindow)

        #禁用word,wps,記事本等文字編輯器處理序
        self.jinyong = True
        import psutil
        import os
        import os.path
        import time
        import threading
        def funcJinyong():
            while self.jinyong:
                for pid in psutil.pids():
                    try:
                            p = psutil.Process(pid)
                            if os.path.basename(p.exe()).lower() in ('notepad.exe', 'winword.exe', 'wps.exe', 'wordpad.exe', 'iexplore.exe', 'chrome.exe', 'qqbrowser.exe', '360chrome.exe', '360se.exe', 'sogouexplorer.exe', 'firefox.exe', 'opera.exe', 'maxthon.exe', 'netscape.exe', 'baidubrowser.exe', '2345Explorer.exe'):
                                    p.kill()
                    except:
                            pass
                ctypes.windll.user32.OpenClipboard(None)
                ctypes.windll.user32.EmptyClipboard()
                ctypes.windll.user32.CloseClipboard()
                time.sleep(1)
        t_jinyong = threading.Thread(target=funcJinyong)
        t_jinyong.start()
        
        #從伺服器接收課程名稱清單，並以下拉式清單顯示
        data = conn.recv(1024)
        data = data.decode()
        kechengQingdan = data.split(',')
        labelKechengmingcheng = tkinter.Label(self.top, text='請選擇課程名稱：')
        labelKechengmingcheng.place(x=10, y=10, height=20, width=100)
        comboboxKechengmingcheng = tkinter.ttk.Combobox(self.top, values=kechengQingdan)
        comboboxKechengmingcheng.place(x=120, y=10, height=20, width=130)
        #每次改變課程名稱時，把self.currentID重新設為0
        def comboxboxKechengmingChanged(event):
            self.currentID = 0
        comboboxKechengmingcheng.bind('<<ComboboxSelected>>', comboxboxKechengmingChanged)

        #課程名稱
        string_Kecheng = tkinter.StringVar(self.top, value='')
        labelKecheng = tkinter.Label(self.top,text='', textvariable=string_Kecheng)
        labelKecheng.place(x=10, y= 40, height=20, width=100)

        #已做多少題
        string_total = tkinter.StringVar(self.top, value='')
        labelTotal = tkinter.Label(self.top, text='', textvariable=string_total)
        labelTotal.place(x=120, y=40, height=20, width=100)
        
        entryMessage = tkinter.scrolledtext.ScrolledText(self.top, wrap=tkinter.WORD)#問題內容
        entryMessage.place(x=10, y=70, width=280, height=70)
        
        def buttonNextClick():#下一題
            kechengmingchengSelected = comboboxKechengmingcheng.get()
            if not kechengmingchengSelected:
                tkinter.messagebox.showerror('很抱歉', '請選擇課程名稱！')
                return

            
            #必須做這道題
            if entryMessage.get(0.0).strip()!='' and entryDaan.get().strip()=='':
                tkinter.messagebox.showinfo('很抱歉', '必須做這道題！')
                return

            #檢查答案長度，禁止向伺服器傳送太長的內容
            if len(entryDaan.get()) >= 200:
                tkinter.messagebox.showerror('很抱歉', '答案太長！')
                return

            #提交答案，同時抓取下一題
            message = kechengmingchengSelected+'xx'+str(self.currentID)+'xx'+entryDaan.get()+'xxnext'
            conn.sendall(message.encode())
            data = conn.recv(1024)
            data = data.decode()
            if data.startswith('no,'):
                fenshu = data.split(',')[1]
                tkinter.messagebox.showinfo(title='恭喜', message='你已經完成考試，得分：'+fenshu)
                buttonNext['state'] = 'disabled'#禁用按鈕
                #結束禁用word，wps，記事本處理序的執行緒
                self.jinyong = False
                return
            #print(data)
            kechengmingcheng, zhangjie, timu, self.currentID, total = data.split('xx')
            entryMessage.delete(0.0, tkinter.END)		#刪除原來的題目內容
            entryMessage.insert(tkinter.INSERT, timu)	#顯示新題目內容
            string_Kecheng.set(kechengmingcheng)
            entryDaan.delete(0, tkinter.END)   #刪除上一題學生輸入的答案
            string_total.set('已答 '+str(total)+' 道題')
        buttonNext = tkinter.Button(self.top, text='下一題', command=buttonNextClick)
        buttonNext.place(x=10, y=150, width=60, height=20)

        #填寫答案的文字框
        entryDaan = tkinter.Entry(self.top,)
        entryDaan.place(x=10,y=180, width=270, height=20)
        
        #預設開啟第一題
        buttonNextClick()

def buttonKaoshiClick():
    xuehao = entryXuehao.get()
    xingming = entryXingming.get()
    serverIP = entryServerIP.get()
    if not re.match('(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}', serverIP):
        tkinter.messagebox.showerror('很抱歉', '伺服器IP位址不合法！')
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((serverIP, 18003))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉', '現在不是考試時間！')
        return
    #向伺服端傳送學號和姓名
    sock.sendall((xuehao+','+xingming).encode())
    #等待伺服器回應，檢查學號與姓名是否相符
    data = sock.recv(1024)
    data = data.decode()
    data = data.strip()
    if data.lower() == 'notmatch':
        tkinter.messagebox.showerror('很抱歉', '學號與姓名不符合！')
        sock.close()
        return
    
    #開啟考試視窗
    int_windowKaoshi.set(1)
    w = windowKaoshi(root, sock, xuehao+','+xingming)
    buttonZice.wait_window(w.top)
    int_windowKaoshi.set(0)
buttonKaoshi = tkinter.Button(root, text='考試', command=buttonKaoshiClick)
buttonKaoshi.place(x=230, y=120, width=40, height=20)

## =============================
# 以下部分程式碼用來接收螢幕廣播

# 使用TCP接收廣播
def receiveBroadCast():
    # 抓取螢幕尺寸，建立填滿螢幕的無標題欄視窗
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    top = tkinter.Toplevel(root,
                           width=screenWidth,
                           height=screenHeight)
    top.overrideredirect(True)
    # 頂端顯示
    top.attributes('-topmost', 1)
    # 建立畫布，用來顯示圖形
    canvas = tkinter.Canvas(top,
                            bg='white',
                            width=screenWidth,
                            height=screenHeight)
    canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverIP = entryServerIP.get()
    # 連接伺服器10001連接埠，失敗直接返回
    try:
        sock.connect((serverIP, 10001))
    except:
        print('error')
        top.destroy()
        return
    
    # 接收伺服器指令
    # *****表示開始傳輸一個新的截圖
    # #####表示本次廣播結束
    while True:
        data = sock.recv(5)
        if data == b'*****':
            # 接收伺服器送來的一幅圖形
            # 圖形大小，位元組總數量
            len_head = struct.calcsize('I32sI')
            data = sock.recv(len_head)
            length, size, sizeLength = struct.unpack('I32sI', data)
            length = int(length)
            size = eval(size[:int(sizeLength)])

            rest = length
            image = []
            while True:
                if rest == 0:
                    break
                elif rest > 40960:
                    temp = sock.recv(40960)
                    rest -= len(temp)
                    image.append(temp)
                else:
                    temp = sock.recv(rest)
                    rest -= len(temp)
                    image.append(temp)
            image = b''.join(image)
            # 更新显示
            image = Image.frombytes('RGB', size, image)
            image = image.resize((screenWidth, screenHeight))
            image = ImageTk.PhotoImage(image)

##            try:
##                canvas.delete(imageId)
##            except:
##                pass

            imageId = canvas.create_image(screenWidth//2, screenHeight//2, image=image)
            
        elif data == b'#####':
            # 廣播結束
            break

    # 本次廣播結束，關閉視窗
    sock.close()
    top.destroy()

# 使用UDP監聽，等待伺服器的廣播指令
def udpListen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 監聽本機10000連接埠
    sock.bind(('',10000))
    while True:        
        data, addr = sock.recvfrom(100)
        # 收到伺服器送來的廣播指令
        if data == b'startBroadCast':
            threading.Thread(target=receiveBroadCast).start()
        elif data == b'shutdown':
            import platform
            if platform.platform().startswith('Windows'):
                command = r'shutdown /s /f'
                os.system(command)
    sock.close()
threading.Thread(target=udpListen).start()
# 螢幕廣播程式結束
## =============================

root.mainloop()          #啟動主迴圈

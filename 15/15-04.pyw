import tkinter
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.colorchooser
from PIL import Image

app = tkinter.Tk()
app.title('My Paint----by Dong Fuguo')
app['width'] = 800
app['height'] = 600

#控制是否允許畫圖的變數，1：允許，0：不允許
yesno = tkinter.IntVar(value=0)
#控制畫圖類型的變數，1：曲線，2：直線，3：矩形，4：文字，5：橡皮
what = tkinter.IntVar(value=1)
#記錄滑鼠位置的變數
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
#前景顏色
foreColor = '#000000'
backColor = '#FFFFFF'

#建立畫布
image = tkinter.PhotoImage()
canvas = tkinter.Canvas(app, bg='white', width=800, height=600)
canvas.create_image(800, 600, image=image)
#按一下滑鼠左鍵，允許畫圖
def onLeftButtonDown(event):
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get()==4:
        #輸出文字
        canvas.create_text(event.x, event.y, text=text)
canvas.bind('<Button-1>', onLeftButtonDown)

#記錄最後繪製的圖形id
global lastDraw
lastDraw = 0
#按住滑鼠左鍵移動，畫圖
def onLeftButtonMove(event):
    if yesno.get()==0:
        return
    if what.get()==1:
        #以目前選擇的前景顏色繪製曲線
        canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
        X.set(event.x)
        Y.set(event.y)
    elif what.get()==2:
        #繪製直線，先刪除剛剛畫過的直線，再畫一條新的直線
        global lastDraw
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                     fill=foreColor)
    elif what.get()==3:
        #繪製矩形，先刪除剛剛畫過的矩形，再畫一個新的矩形
        #global lastDraw
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, fill=backColor, outline=foreColor)
    elif what.get()==5:
        #橡皮擦，以背景色填充10*10的矩形區域
        canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, outline=backColor, fill=backColor)
canvas.bind('<B1-Motion>', onLeftButtonMove)

#釋放滑鼠左鍵，不允許畫圖
def onLeftButtonUp(event):
    if what.get()==2:
        #繪製直線
        canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    elif what.get()==3:
        #繪製矩形
        canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, fill=backColor, outline=foreColor)
    yesno.set(0)
    global lastDraw
    lastDraw = 0
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

#建立選單
menu = tkinter.Menu(app, tearoff=0)
#開啟影像檔
def Open():
    filename = tkinter.filedialog.askopenfilename(title='Open Image', filetypes=[('image', '*.jpg *.png *.gif')])
    if filename:
        global image
        image = tkinter.PhotoImage(file=filename)
        canvas.create_image(80, 80, image=image)
menu.add_command(label='Open', command=Open)
#加入功能表，清除繪製的所有圖形
def Clear():
    for item in canvas.find_all():
        canvas.delete(item)
menu.add_command(label='Clear', command=Clear)
#加入分隔線
menu.add_separator()
#建立子功能表，用來選擇繪圖類型
menuType = tkinter.Menu(menu, tearoff=0)
def drawCurve():
    what.set(1)
menuType.add_command(label='Curve', command=drawCurve)
def drawLine():
    what.set(2)
menuType.add_command(label='Line', command=drawLine)
def drawRectangle():
    what.set(3)
menuType.add_command(label='Rectangle', command=drawRectangle)
def drawText():
    global text
    text = tkinter.simpledialog.askstring(title='Input what you want to draw', prompt='')
    what.set(4)
menuType.add_command(label='Text', command=drawText)
menuType.add_separator()
#選擇前景顏色
def chooseForeColor():
    global foreColor
    foreColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Foreground Color', command=chooseForeColor)
#選擇背景顏色
def chooseBackColor():
    global backColor
    backColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Background Color', command=chooseBackColor)
#橡皮擦
def onErase():
    what.set(5)
menuType.add_command(label='Erase', command=onErase)
menu.add_cascade(label='Type', menu=menuType)

#釋放滑鼠右鍵，在滑鼠位置彈出選單
def onRightButtonUp(event):
    menu.post(event.x_root, event.y_root)
canvas.bind('<ButtonRelease-3>', onRightButtonUp)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

app.mainloop()

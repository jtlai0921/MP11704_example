import tkinter
import time

app = tkinter.Tk()
app.title('tkinter animation')
app['width'] = 800
app['height'] = 600
canvas = tkinter.Canvas(app, bg='white', width=800, height=600)
#開啟與載入圖片
image = tkinter.PhotoImage(file='open.png')
#記下圖片的編號
id_actor = canvas.create_image(80, 80, image=image)
#控制是否自動運動的變數
flag = False
#按一下滑鼠左鍵，角色開始運動
def onLeftButtonDown(event):
    global flag
    flag = True
    while flag:
        #id_actor表示要運動的圖形編號
        #第二個參數表示x方向的移動距離，5代表向右移動5個像素
        #第三個參數表示y方向的移動距離，0代表不移動
        canvas.move(id_actor, 5, 0)
        canvas.update()
        time.sleep(0.05)
canvas.bind('<Button-1>', onLeftButtonDown)

def onRightButtonUp(event):
    global flag
    flag = False
canvas.bind('<ButtonRelease-3>', onRightButtonUp)

#支援鍵盤上的四個方向鍵控制圖片的運動方向
def keyControl(event):
    if event.keysym == 'Up':
        canvas.move(id_actor, 0, -5)
        canvas.update()
    elif event.keysym == 'Down':
        canvas.move(id_actor, 0, 5)
        canvas.update()
    elif event.keysym == 'Left':
        canvas.move(id_actor, -5, 0)
        canvas.update()
    elif event.keysym == 'Right':
        canvas.move(id_actor, 5, 0)
        canvas.update()
canvas.bind_all('<KeyPress-Up>', keyControl)
canvas.bind_all('<KeyPress-Down>', keyControl)
canvas.bind_all('<KeyPress-Left>', keyControl)
canvas.bind_all('<KeyPress-Right>', keyControl)

canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
canvas.focus()
#啟動主迴圈
app.mainloop()

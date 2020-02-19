import sys
import tkinter as Tk
import matplotlib
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

matplotlib.use('TkAgg')

root = Tk.Tk()
root.title("matplotlib in TK")
#設定圖形尺寸與品質
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3, 0.01)
s = sin(2*pi*t)
#繪製圖形
a.plot(t, s)


#把繪製的圖形顯示到tkinter視窗
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#把matplotlib繪製圖形的工具列顯示於tkinter視窗
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#定義並繫結鍵盤事件處理函數
def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)
canvas.mpl_connect('key_press_event', on_key_event)

#按一下事件處理函數
def _quit():
    #結束事件主迴圈，並銷毀應用程式視窗
    root.quit()
    root.destroy()
button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()

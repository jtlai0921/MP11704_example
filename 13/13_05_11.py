from random import choice
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button

t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

#定義允許的幾種頻率，並建立單選鈕元件
#其中[0.05, 0.7, 0.15, 0.15]表示元件在視窗的歸一化位置和大小
axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))
hzdict = {'2 Hz': s0, '4 Hz': s1, '8 Hz': s2}
def hzfunc(label):
    ydata = hzdict[label]
    l.set_ydata(ydata)
    plt.draw()
radio.on_clicked(hzfunc)

#定義允許的幾種顏色，並建立單選鈕元件
rax = plt.axes([0.05, 0.4, 0.15, 0.15], axisbg=axcolor)
colors = ('red', 'blue', 'green')
radio2 = RadioButtons(rax, colors)
def colorfunc(label):
    l.set_color(label)
    plt.draw()
radio2.on_clicked(colorfunc)

#定義允許的幾種線型，並建立單選鈕元件
rax = plt.axes([0.05, 0.1, 0.15, 0.15], axisbg=axcolor)
styles = ('-', '--', '-.', 'steps', ':')
radio3 = RadioButtons(rax, styles)
def stylefunc(label):
    l.set_linestyle(label)
    plt.draw()
radio3.on_clicked(stylefunc)

#定義按鈕按一下事件處理函數，並在視窗上建立按鈕
def randomFig(event):
    #隨機選擇一個頻率，同時設定單選鈕的選中項
    hz = choice(tuple(hzdict.keys()))
    hzLabels = [label.get_text() for label in radio.labels]
    radio.set_active(hzLabels.index(hz))
    l.set_ydata(hzdict[hz])
    #隨機選擇一個顏色，同時設定單選鈕的選中項
    c = choice(colors)
    radio2.set_active(colors.index(c))
    l.set_color(c)
    #隨機選擇一個線型，同時設定單選鈕的選中項
    style = choice(styles)
    radio3.set_active(styles.index(style))
    l.set_linestyle(style)
    #根據設定的屬性繪製圖形
    plt.draw()
axRnd = plt.axes([0.5, 0.015, 0.2, 0.045])
buttonRnd = Button(axRnd, 'Random Figure')
buttonRnd.on_clicked(randomFig)
#顯示圖形
plt.show()

from time import sleep
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()
#設定圖形顯示位置
plt.subplots_adjust(bottom=0.2)
#實驗資料
range_start, range_end, range_step = 0, 1, 0.005
t = np.arange(range_start, range_end, range_step)
s = np.sin(4*np.pi*t)
l, = plt.plot(t, s, lw=2)
#自訂類別，用來封裝兩個按鈕的按一下事件處理函數
class ButtonHandler:
    def __init__(self):
        self.flag = True
        self.range_s, self.range_e, self.range_step = 0, 1, 0.005
    #執行緒函數，用來更新資料並重新繪製圖形
    def threadStart(self):
        while self.flag:
            sleep(0.02)
            self.range_s += self.range_step
            self.range_e += self.range_step
            t = np.arange(self.range_s, self.range_e, self.range_step)
            ydata = np.sin(4*np.pi*t)
            #更新資料
            l.set_xdata(t-t[0])
            l.set_ydata(ydata)
            #重新繪製圖形
            plt.draw()
    def Start(self, event):
        self.flag = True
        #建立並啟動新執行緒
        t = Thread(target=self.threadStart)
        t.start()
    def Stop(self, event):
        self.flag = False
        
callback = ButtonHandler()
#建立按鈕，並設定按一下事件處理函數
axprev = plt.axes([0.81, 0.05, 0.1, 0.075])
bprev = Button(axprev, 'Stop')
bprev.on_clicked(callback.Stop)
axnext = plt.axes([0.7, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Start')
bnext.on_clicked(callback.Start)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
#設定繪圖區域位置
plt.subplots_adjust(left=0.1, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
#初始振幅與頻率，並繪製初始圖形
a0, f0= 5, 3
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red')
#設定坐標軸刻度範圍
plt.axis([0, 1, -10, 10])

axColor = 'lightgoldenrodyellow'
#建立兩個Slider元件，分別設定位置/尺寸、背景色和初始值
axfreq = plt.axes([0.1, 0.1, 0.75, 0.03], axisbg=axColor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
axamp = plt.axes([0.1, 0.15, 0.75, 0.03], axisbg=axColor)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
#為Slider元件設定事件處理函數
def update(event):
    #取得Slider元件的目前值，並以此更新圖形
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    plt.draw()
    #fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)

#建立Adjust按鈕，設定大小、位置和事件處理函數
def adjustSliderValue(event):
    ampValue = samp.val + 0.05
    if ampValue > 10:
        ampValue = 0.1
    samp.set_val(ampValue)

    freqValue = sfreq.val + 0.05
    if freqValue > 30:
        freqValue = 0.1
    sfreq.set_val(freqValue)
    update(event)
axAdjust = plt.axes([0.6, 0.025, 0.1, 0.04])
buttonAdjust = Button(axAdjust, 'Adjust', color=axColor, hovercolor='red')
buttonAdjust.on_clicked(adjustSliderValue)

#建立按鈕元件，以便恢復初始值
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axColor, hovercolor='yellow')
def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

plt.show()

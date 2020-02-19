import numpy as np
import pylab as pl
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\msjh.ttf') #設定字體
t = np.arange(0.0, 2.0*np.pi, 0.01)	#引數取值範圍
s = np.sin(t)						#計算正弦函數值
z = np.cos(t)						#計算餘弦函數值
pl.plot(t, s, label='正弦')
pl.plot(t, z, label='餘弦')
pl.xlabel('x-變數', fontproperties=myfont, fontsize=16)		#設定x標籤
pl.ylabel('y-正弦餘弦函數值', fontproperties=myfont, fontsize=16)
pl.title('sin-cos函數圖形', fontproperties=myfont, fontsize=24) #圖形標題
pl.legend(prop=myfont)				#設定圖例
pl.show()

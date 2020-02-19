import numpy as np
import pylab as pl

t = np.arange(0.0, 2.0*np.pi, 0.01)	#產生陣列，0到2π之間，以0.01為步長
s = np.sin(t)			#對陣列的所有元素求正弦值，得到新陣列
pl.plot(t,s)			#畫圖，以t為橫坐標，s為縱坐標
pl.xlabel('x')			#設定坐標軸標籤
pl.ylabel('y')
pl.title('sin')		#設定圖形標題
pl.show()				#顯示圖形

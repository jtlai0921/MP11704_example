import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 2*np.pi, 500)	#建立引數陣列
y1 = np.sin(x)					#建立函數值陣列
y2 = np.cos(x)
y3 = np.sin(x*x)
plt.figure(1)					#建立圖形
#create three axes
ax1 = plt.subplot(2,2,1)			#第一列第一行圖形
ax2 = plt.subplot(2,2,2)			#第一列第二行圖形
ax3 = plt.subplot(2,1,2)			#第二列
plt.sca(ax1)					#選擇ax1
plt.plot(x,y1,color='red')		#繪製紅色曲線
plt.ylim(-1.2,1.2)				#限制y坐標軸範圍
plt.sca(ax2)					#選擇ax2
plt.plot(x,y2,'b--')			#繪製藍色曲線
plt.ylim(-1.2,1.2)
plt.sca(ax3)					#選擇ax3
plt.plot(x,y3,'g--')
plt.ylim(-1.2,1.2)
plt.show()

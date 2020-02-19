import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)
z = np.cos(x*x)
plt.figure(figsize=(8,5))
#標籤前後加上$，代表以內嵌的LaTex引擎顯示為公式
plt.plot(x,y,label='$sin(x)$',color='red',linewidth=2)	#紅色，2個像素寬
plt.plot(x,z,'b--',label='$cos(x^2)$')		#藍色，虛線
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Sin and Cos figure using pyplot')
plt.ylim(-1.2,1.2)
plt.legend()							#顯示圖例
plt.show()

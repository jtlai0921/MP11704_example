import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y = np.mgrid[-2:2:20j, -2:2:20j]
z = 50 * np.sin(x+y)		#測試資料
ax = plt.subplot(111, projection='3d')	#三維圖形
ax.plot_surface(x,y,z,rstride=2, cstride=1, cmap=plt.cm.Blues_r)
ax.set_xlabel('X')			#設定坐標軸標籤
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
#need to pip install matplotlib first

image = misc.ascent()		#二維圖形陣列，lena圖形
w = np.zeros((50, 50))		#全0二維陣列，摺積核
w[0][0] = 1.0				#修改參數，調整濾波器
w[49][25] = 1.0				#可以根據需求調整
image_new = signal.fftconvolve(image, w)	#使用FFT演算法進行摺積

plt.figure()
plt.imshow(image_new)		#顯示濾波後的圖形
plt.gray()
plt.title('Filtered image')
plt.show()

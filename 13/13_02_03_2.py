import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
#need to pip install matplotlib first

image = misc.ascent()
w = signal.gaussian(50, 10.0)
image_new = signal.sepfir2d(image, w, w)

plt.figure()
plt.imshow(image_new)		#顯示濾波後的圖形
plt.gray()
plt.title('Filtered image')
plt.show()

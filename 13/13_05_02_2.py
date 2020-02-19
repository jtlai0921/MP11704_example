import matplotlib.pylab as pl
import numpy as np

x = np.random.random(100)
y = np.random.random(100)
pl.scatter(x,y,s=x*500,c=u'r',marker=u'*')	#s指大小，c指顏色，marker指符號形狀
pl.show()

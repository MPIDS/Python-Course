import pylab as pl
import numpy as np

x = np.arange(0,3,0.01)
line, = pl.plot ( x, np.sin(x), 'rD', markersize=5., label = "sin(x)" )
pl.legend()
pl.grid()

pl.show()

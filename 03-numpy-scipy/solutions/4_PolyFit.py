# 4. Polynomial Fit

import numpy as np
import scipy as sc
import pylab as pl
x = np.arange(-4, 4, 0.1)
y = -3.*x**3 + 2.*x - 8

print sc.polyfit(x, y, 3) # polynomial fit of order 3

y = y + np.random.randn(len(y))*10 # Gaussian noise of variance 10 added to the function
coeff= sc.polyfit(x, y, 3)
pl.plot(x, y, label = 'function + noise')
pl.plot(x, coeff[0]*x**3 + coeff[1]*x**2 + coeff[2]*x + coeff[3], label = 'PolyFit3', color = 'red')
pl.legend()
pl.show()


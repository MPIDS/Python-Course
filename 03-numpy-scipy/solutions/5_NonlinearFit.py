# 5. Nonlinear Fit

import numpy as np
f = lambda x, a, b : np.exp(-a*x) + b # define a lambda function with three arguments

x = np.arange(0, 4, 0.01)
y = f(x, 2.5, 1.4) # generate y values from the lambda function
y = y + 0.25*np.random.randn(len(y)) # add Gaussian noise to the values

import pylab as pl
pl.plot(x, y)
pl.show()

import scipy.optimize as opt

# NOTE: The optimize package is NOT automatically included when you import scipy as sc.
# The function 'optimize.curve_fit' is for fitting a function f(x) to data coordinates (x, y) and returns the fitted parameters to 'popt'.
# For further information try 'help(opt.curve_fit)'.

popt, pcov = opt.curve_fit(f, x, y)
print popt

pl.plot(x, y, label = 'Noisy Data')
pl.plot(x, f(x, popt[0], popt[1]), label = 'Nonlinear Fit', color = 'r')
pl.annotate('$f(x) = e^{-a \cdot x} + b$', size = 16, 
								xy=(1, 1.5),  xycoords = 'data',
                xytext=(1, 2.5), textcoords = 'data',
                arrowprops=dict(arrowstyle="->") )
pl.xlabel('x')
pl.ylabel('f(x)')
pl.legend()
pl.show()


# 6. Intergration in Python

import numpy as np
f = lambda x : np.exp(-(x + 3)**2)
# try: f([0, 1, 2, 3]) # -> you will see that the function doesn't take lists as arguments, only 'f(np.arange(1,4))' would work

# Vectorize the function f and try again :)

f = np.vectorize(f)
f([0, 1, 2, 3])

# Define an integration function 'intf', using the Riemann sum

intf = lambda fr, to, step : f(np.arange(fr, to, step)).sum()*step

for i in [1, 0.1, 0.01, 0.001]:
    print '%1.12g, result of the Riemann sum in steps of %1.3g' % (intf(-20, 20, i), i)

# Now integrate by using the function scipy.integrate.quad().
# This function returns the result of the integration and its estimated error.

import scipy.integrate as int
int.quad(f, -20, 20)

int.quad(lambda x: 1./x, 1., np.Inf)

# NOTE: The integral of 1/x from 1 to infinity diverges to infinity! Therefore the estimated error is very large.

int.quad(lambda x: 1./x**2, 1., np.Inf)


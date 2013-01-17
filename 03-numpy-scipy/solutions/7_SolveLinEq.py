# 7. Solving systems of linear equations

# First create the matrix of fruit quantities.

import numpy as np
Fruits = np.array([[10, 5, 1], [1, 8, 1], [9, 3, 5]])
print Fruits

# Then create a vector of the total prices.

total_prices = np.array([35.35, 24.91, 40.38])
print total_prices

# Obtain the price of each fruit by solving the linear system total_prices = Fruits * singel_prices

import scipy.linalg as la
single_prices = la.solve(Fruits, total_prices)
print single_prices

# Proof your results!

print np.dot(Fruits, single_prices)


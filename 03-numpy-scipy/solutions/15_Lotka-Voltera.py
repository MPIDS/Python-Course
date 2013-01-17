# 15. Lotka-Voltera system

# Define the system of ordinary differential equations.

import numpy as np
import scipy.optimize as opt

def dN_dt (N, t0, eps1, gamma1, eps2, gamma2):
    dN1_dt = N[0] * (eps1 - gamma1*N[1])
    dN2_dt = -N[1] * (eps2 - gamma2*N[0])
    return np.array([dN1_dt, dN2_dt])

# Return the growth rates after the first iteration.

print 'Growth rates after first iteration of initial values N1 = 10 and N2 = 5'
print 'Parameters are eps1 = 1, gamma1 = 0.1, eps2 = 1.5, gamma2 = 0.075'
print dN_dt([10., 5.], 0., 1., 0.1, 1.5, 0.075)

# Find the fixed points by searching for stable solutions. Try different inital values of N1 and N2 (x0 = [N1, N2]).

print 'Fixed points of the system'
print opt.fsolve(dN_dt, x0 = [0, 0], args = (0, 1.0, 0.1, 1.5, 0.075))
print opt.fsolve(dN_dt, x0 = [10, 10], args = (0, 1.0, 0.1, 1.5, 0.075))

# Check the fixed points. Zero growth rate means that the solution is stable.

print 'Growth rates of the fixed points'
print dN_dt([0., 0.], 0., 1.0, 0.1, 1.5, 0.075)
print dN_dt([20., 10.], 0., 1.0, 0.1, 1.5, 0.075)

# Solve the system of ODEs by integrating with scipy.integrate.odeint
# First determine time resolution and start values.

import scipy.integrate as int

times_1 = np.arange(0, 15, 1.)
times_001 = np.arange(0, 15, 0.001)
N_0 = np.array([10, 5])

# Then solve the system for different time resolution.

sol_1 = int.odeint(dN_dt, N_0, times_1, args = (1.0, 0.1, 1.5, 0.075))
sol_001 = int.odeint(dN_dt, N_0, times_001, args = (1.0, 0.1, 1.5, 0.075))
print 'Number of data points of the two solutions obtained in time steps of 1 and 0.001'
print sol_1.shape
print sol_001.shape # to compare the number of data points of the solutions

# Compare the two solutions in a plot.

import pylab as pl

pl.plot(times_1, sol_1[:, 0], label = 'Prey, $\Delta t=1$', color = [0, 0.5, 1], linewidth = 2)
pl.plot(times_001, sol_001[:, 0], label = 'Prey, $\Delta t=0.001$', color = 'b', linewidth = 2, alpha = 0.7)
pl.plot(times_1, sol_1[:, 1], label = 'Predator, $\Delta t=1$', color = [1, 0.5, 0], linewidth = 2)
pl.plot(times_001, sol_001[:, 1], label = 'Predator, $\Delta t=0.001$', color = 'r', linewidth = 2, alpha = 0.7)
pl.axis([0, 15, 0, 60])
pl.xlabel('Time')
pl.ylabel('Population')
pl.title('Predator-Prey Evolution', size = 14)
pl.legend(loc = 2, prop = {'size':10}, labelspacing = 0)
pl.show()


#!/usr/bin/env python
import numpy as np
import pylab as plt

t = np.arange(0.0, 1.01, 0.01)
s = np.sin(2*np.pi*t)

plt.subplot(2,1,1)
plt.plot (t, s*np.exp(-5*t), 'b', label= r'$sin (2\pi t) e^{-5 t}$', linewidth=4. )
plt.fill(t, s*np.exp(-5*t), 'r')
plt.xlabel( 'time')
plt.ylabel( 'position')
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot (t, np.sin(2.*np.pi*t), 'b', label= r'$sin (2\pi t)$', linewidth=4. )
plt.plot (t, np.cos(2.*np.pi*t), 'b', label= r'$cos (2\pi t)$', linewidth=4. )
plt.fill_between(t,np.cos(2.*np.pi*t) , np.sin(2.*np.pi*t), color='green')
plt.xlabel( 'time')
plt.legend()
plt.grid(True)

plt.show()


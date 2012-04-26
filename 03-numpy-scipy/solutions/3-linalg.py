import numpy as np
import pylab as pl
import scipy.linalg as la

# (a)
geteig = lambda N : la.eigvals(np.random.randn(N,N))
M = geteig (1000)
pl.figure()
pl.plot ( np.real(M), np.imag(M), 'ko',markersize=5,  label = r'$N = 1000$')
titletxt = pl.title ( 'Eigenvalues of a random matrix')
titletxt.set_fontsize(24)
titletxt.set_color('red')

pl.xlabel ( 'real part')
pl.ylabel ( 'imag part' )
pl.legend()
pl.savefig ('matrix1.eps')

# (c)
isInCircle = lambda x,y,r : np.sqrt(x**2 + y**2) < r
minRadius = lambda M : np.sqrt(np.real(M)**2 + np.imag(M)**2).max()

# (d) 

fig = pl.figure()
graph = fig.add_subplot(111)

import matplotlib.patches as pt

Ns = [200, 500, 1000][::-1]
colors = ['yellow', 'green', 'black', 'yellow', 'black']
for i in range(len(Ns)):
  M = geteig (Ns[i]) 
  R = minRadius (M)
  graph. plot (  np.real(M), np.imag(M), 'o', color = colors[i] , markersize=5,  label = r'$N = '+str(Ns[i])+'$' )
  circ = pt.Circle ( (0,0), R, color = colors[i], alpha = 0.3 )
  graph.add_patch (circ)

pl.legend()
pl.savefig ('matrix2.pdf')
pl.show()


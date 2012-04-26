import numpy as np
import cdtw
import plotdtw

dt=0.2
M=plotdtw.getexamplematrix(dt)
p=cdtw.cdtw(M)

plotdtw.plotdtw( M, np.row_stack((p[1,:],p[0,:])))

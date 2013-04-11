from dtw_python import dtw
import cdtw 

import numpy as np
from plotdtw import *
import time
import pylab as pl


runit =False

if runit:
    dts=np.array([1,0.5,0.2,.1,.06,.03,.025,.02,.015,.01,.008,.007])
    ns=np.zeros(dts.shape)
    ptimes=np.zeros(dts.shape)
    ctimes=np.zeros(dts.shape)


    for i in range(len(dts)):
        M=getexamplematrix( dts[i] )
        ns[i]=M.shape[0]
        print "N=%i"%ns[i]
        start=time.time()
        dtw(M)
        end=time.time()
        ptimes[i]=end-start

        start=time.time()
        cdtw.cdtw(M)
        end=time.time()
        ctimes[i]=end-start


plt.subplot(2,1,1)
pl.plot( ns,ptimes, '*-', color="blue", linewidth=4, label="python")
pl.plot( ns,ctimes, '*-', color="red", linewidth=4, label="c")
#pl.xlabel( 'matrix size')
pl.ylabel( 'runtime (sec)')
#lpl.legend()

plt.subplot(2,1,2)
pl.plot( ns,np.sqrt(ptimes), '*-', color="blue", linewidth=4, label="python")
pl.plot( ns,np.sqrt(ctimes), '*-', color="red", linewidth=4, label="c")
pl.xlabel( 'matrix size')
pl.ylabel( r'sqrt(runtime)')
pl.legend(loc="upper left")

pl.show()
    

    

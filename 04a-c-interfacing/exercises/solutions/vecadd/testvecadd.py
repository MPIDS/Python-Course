import vecadd
import numpy as np

x1=np.arange(1,10,dtype=np.float32)
x2=np.arange(1,10, dtype=np.float32)
x3=np.zeros(len(x1), dtype=np.float32)

vecadd.vecadd2( x1, x2, x3 )
print x3


print vecadd.vecadd( x1, x2 )

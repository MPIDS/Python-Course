import numpy as np
num=715827883
f=np.vectorize( lambda x,n: n%x==0 )
a=np.arange(2,num)
z=f(a)

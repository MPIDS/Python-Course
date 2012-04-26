import numpy as np
import pylab as pl

# (a)
dice = np.vectorize( lambda N : np.sum( (np.random.randint(1,7, (N,2) )==6).sum(axis=1)>0) )
prop = np.vectorize( lambda N : 1. * dice(N) / N )

# (b)
x = np.arange (5, 30000, 100 )
y = prop ( x )

pl.figure()
pl.semilogx (x, y)


# (c)
dist = lambda N,Z : dice ( [N]*Z )
data = dist (N=1000, Z=10000)

pl.figure()
pl.hist( data, bins = np.arange (data.min(), data.max(), 1) )
print "Mean value :" +str( data.mean() )
print "Std  value :" +str( data.std() )

# (d)
def geterrordata ( N, Z ):
  data = prop ( [N] * Z )
  mu  = data.mean()
  sgm = data.std()

  return (N, mu,sgm)

N = np.arange ( 1, 20, 1 )
data = np.zeros( (len(N), 3) )

for i in range (len (N)):
  data[i] = geterrordata ( N[i], 5000 )

pl.figure()
pl.plot     ( data[:,0], data[:,1], 'ko' )
pl.errorbar ( data[:,0], data[:,1], data[:,2], color = 'black' )


pl.show()


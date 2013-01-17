import numpy as np
import pylab as pl

MAX = 80
def histgram( data, numbins ):
  border = np.linspace ( data.min(), data.max() , numbins+1)
  midpoints = border[:-1] + 0.5*np.diff(border)[0]
  anz = np.zeros( midpoints.shape )
  
  for i in range(len(border) - 2):
    anz[i] = np.sum( (data>= border[i] ) & (data<border[i+1]) )
  anz[-1] = np.sum( (data>= border[-2] )  )

  return (midpoints, anz)

def histgram2( data, numbins ):
  border = np.linspace ( data.min(), data.max() , numbins+1)
  anz = np.zeros( len (border)-1 )

  for i in range(len(border) - 2):
    anz[i] = np.sum( (data>= border[i] ) & (data<border[i+1]) )
  anz[-1] = np.sum( (data>= border[-2] )  )

  return (border[:-1], anz, np.diff(border)[0] )


def drawhistgram( h ):
    for i in range( len(h[0]) ):
        print "% 4.2f "%h[0][i], "*" * int((h[1][i]/float(max(h[1])))*MAX);


## testing
data= np.random.randn( 1000 )
drawhistgram( histgram( data, 30 ) );

(left, anz, width) = histgram2( data, 30 )

pl.subplot(2,1,1)
pl.bar(left, anz, width=width)

pl.subplot(2,1,2)
pl.hist(data,30)
pl.show()



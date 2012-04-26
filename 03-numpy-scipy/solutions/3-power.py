import numpy as np
import pylab as pl


fs = 0.0001
x = np.arange( 0, 20, fs)
y = np.zeros (x.shape)
freqs = np.random.randint ( 1, 300, 20 )

for freq in freqs:
  y = y + np.sin ( 2. * np.pi * freq * x )

pl.figure()

pl.plot (x,y)
pl.axis ( [0., 2., 1.2*min(y), 1.2* max(y)] )

fig = pl.figure()
data = np.abs(np.fft.fft(y)**2)

for freq in freqs:
  pl.plot ( [freq]*2, [1.2*min(data), 1.2* max(data)], 'r--', linewidth = 4. )

pl.plot ( np.fft.fftfreq( len(y), d=fs), data, 'b-', linewidth = 1. )
pl.axis ([0, 300, 1.2*min(data), 1.2*max(data)] )
pl.xlabel ( r'frequenzy / $Hz$ ' )
pl.ylabel ( r'power ' )

sub1 = fig.add_axes( (0.6, 0.6, 0.38, 0.38 )  )
pl.setp(sub1, xticks=[], yticks=[])

sub2 = fig.add_axes( (0.7, 0.7, 0.25, 0.25 ) )
sub2.plot (x,y)
pl.setp ( sub2, xlim =[0., 2.], ylim =[1.2*min(y), 1.2* max(y)], xlabel = (r'time / $ms$') , ylabel =r'signal $f(t)$')


pl.savefig('power.eps')



pl.show()

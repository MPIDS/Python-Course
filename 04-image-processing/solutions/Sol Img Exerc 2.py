# -*- coding: utf-8 -*-

import scipy.ndimage as ndi
import pylab as pl

from numpy.fft import fft2, ifft2, fftshift, ifftshift
from numpy import log, abs, real, angle

# needed for 2.d
from numpy.random import random_sample
from numpy import pi, sin, cos


##### 2.a
img = ndi.imread('Python.png', flatten = True)

imgFFT = fftshift( fft2( img ) )

pl.gray()

pl.figure(1, figsize=(10,10))         # Creates a figure big enough to show the subplots


pl.subplot(1,3,1)
pl.imshow( abs(imgFFT) )           # Plots just the amplitude
pl.title('Amplitude')

##### 2.b
pl.subplot(1,3,2)
pl.imshow( log(abs(1+imgFFT)) )    # Absolute value
pl.title('Log of Amplitude')

pl.subplot(1,3,3)
pl.imshow( angle(imgFFT) )         # Phase
pl.title('Phase')

# Most power in images is concentrated around zero frequency
# (which represents the mean). This stands out when the amplitude
# is plotted, frustrating our view of the other frequencies. 
# Log helps visualizing data with many different orders of magnitude.

pl.show()


##### 2.c

img2 = real(ifft2( ifftshift( imgFFT ) ))

pl.figure(2)

pl.subplot( 1, 2, 1)
pl.imshow(img)
pl.subplot( 1, 2, 2)
pl.imshow(img2)

pl.show()

print 'The squared error is: ', ((img - img2)**2).sum()
# Yes, they're the same!


##### 2.d

# Using NumPy, we can avoid loops by performing operations in entire
# vectors at the same time. This is calculed vectorial computation
# and is very powerful: besides being easy to read and avoiding loops,
# it is much faster.

randomPhases = random_sample( img.shape )
sinRand = sin( 2 * pi * randomPhases )
cosRand = cos( 2 * pi * randomPhases )

Amplitude = abs( imgFFT )


imgMessedFFT = Amplitude * cosRand  +  Amplitude * sinRand * 1j

imgMessed = real(ifft2( ifftshift( imgMessedFFT ) ))

pl.figure(3)

pl.imshow( imgMessed )

pl.show()

# The figure now has the same power distribution (amplitude) as the original one,
# but the phases are messed up. This destroys the structure in it, although the image
# still feels "natural". Doesn't it look like... clouds?




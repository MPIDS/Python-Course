# -*- coding: utf-8 -*-

import scipy.ndimage as ndi
import pylab as pl 
import numpy as np

from numpy.fft import fft2, ifft2
from numpy import real

from numpy.random import randn # Gaussian random numbers


##### 3.a

img = ndi.imread('Python.png', flatten = True)

# create the filter matrix
K = -1/8. * np.ones([3,3])
K[1,1] = 1

print K


imgConvFFT = fft2( img ) * fft2(K, img.shape)
imgConv = real(ifft2( imgConvFFT ))
pl.imshow( imgConv )
pl.gray()
pl.show()

# This filter works by eliminating what the neighboring pixels
# represent, emphasizing what's different. That's why the borders
# are enhanced, while background and uniform surfaces are diminished.


##### 3.b

# Function to generate a Gaussian filter matrix. A larger shape will
# give better results.
def gaussianFilter (std, shape=[25,25]):
    center = np.floor(np.array(shape)/2.)
    
    [ii,jj] = np.indices(shape)
    rSquared = (ii-center[0])**2 + (jj-center[1])**2  # x**2 + y**2
    filter = np.exp( -rSquared/(2 * std**2) )
    
    return filter/(std * np.sqrt(2 * np.pi))

pl.figure(1)
pl.imshow(gaussianFilter(3))
pl.title('Gaussian filter with std. deviation 3')
pl.show()

##### 3.b / 3.c
pl.figure(2, figsize=[10,10])
sigmas = [1, 3, 5, 7]
ii = 1
for sigma in sigmas:
    imgSmooth = real( ifft2( fft2(img) * fft2( gaussianFilter(sigma), img.shape) ) )
    pl.subplot(2,2,ii)
    pl.imshow(imgSmooth)
    pl.title('Sigma = ' + str(sigma))
    ii += 1


##### 3.d
imgNoisy = img + 100*randn( img.shape[0], img.shape[1] )
pl.imshow(imgNoisy)

##### 3.e
pl.figure(2, figsize=[10,10])

ii = 1
for sigma in [1, 1.3, 1.5, 1.7]:
    imgRecovered = real( ifft2( fft2(imgNoisy) * fft2( gaussianFilter(sigma), img.shape) ) )
    
    pl.subplot(2,2,ii)
    pl.imshow(imgRecovered)
    ii = ii + 1

pl.show()


# -*- coding: utf-8 -*-

import scipy.ndimage as ndi
import pylab as pl
import numpy as np


##### 1.a
    
img = ndi.imread('python.png', flatten = True)
    
##### 1.b

# np.histogram returns the count and range of each bin
[imgHist, bins] = np.histogram( img, 256, (0, 255) )
    
pl.subplot(1,2,1)
pl.bar(range(256), imgHist)
pl.xlim([-10, 260])
pl.show()
    
##### 1.c
img = ndi.imread('python.png');

chColors = ['red', 'green', 'blue']

histograms = []

# calculate histograms
for channel in range(3):
     [hist, bins] = np.histogram(img[:,:,channel], 256, (0,255))
     histograms.append(hist)

# plot histograms
for ch in range(3):
    pl.plot(histograms[ch], color = chColors[ch], label = chColors[ch] )
    
pl.ylim([0, 10000]) # adjusts scale in order to see other colors, because white pixels are much more frequent
pl.legend(loc=0)
pl.show()


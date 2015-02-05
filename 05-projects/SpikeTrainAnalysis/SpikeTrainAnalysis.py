
# coding: utf-8

## Exercises Day 2 - Numpy, Scipy and Matplotlib

# IMPRS Neurosciences - Python Course, June 26, 2013
# 
# Exercise by Norma Kühn

# In this exercise you will learn how to load data from text files, to organize it in numpy arrays and to work with it. You will get introduced to histograms and curve fitting and several other tools from matplotlib and scipy.
# 
# The exercise will guide you through a simple analysis of electrophysiological data recorded from a retinal ganglion cell in the mouse retina by Michael Weick (Gollisch Lab).

### 1. Loading and organizing data

# **Useful functions:** `numpy.loadtxt()`, `pylab.hist()`
# 
# Load the module 'numpy' to load the data.

# In[2]:

import numpy as np


# Load the data from file 'Vtrace.dat' as ascii text and pass it to a variable which you call 'Vtrace'. This might take a few seconds since it is a large data set.

# In[3]:

Vtrace = np.loadtxt('Vtrace.dat')


# This is the voltage trace of a patch clamp recording from a retinal ganglion cell. The trace is sampled with 20 kHz.
# 
# Create a numpy array 'tbins' which contains the time bins of the voltage trace in steps of 0.00005 s. The array should have the same length as the voltage trace.

# In[4]:

tbins = np.arange(0, len(Vtrace-1)/20000., 0.00005)


# The cell responds to a visual stimulus. This stimulus is triggered to the times which you find in 'trigger.dat'. Load this data into the variable 'trigger'.

# In[5]:

trigger = np.loadtxt('trigger.dat')


### 2. Plotting data

# Load the module 'pylab' for plotting.

# In[6]:

import pylab as pl


#### a) Spike detection (and PSTH?)

# Plot the first 5 s of data. Look for a reasonable threshold to detect spikes and add this threshold as a red dashed line to the plot. Don't forget to label the axes and to put a legend in the end.

# In[7]:

pl.plot(tbins[0:100000], Vtrace[0:100000], label = 'V trace')
threshold = -100
pl.plot(tbins[0:100000], np.ones(100000)*threshold, '--r', label = 'Threshold')
pl.xlabel('Time (s)')
pl.ylabel('Voltage (mV)')
pl.legend()


# Now, find the time points where the voltage trace is crossing the threshold from below. 
# 
# The easiest way to do so is to first create a numpy array of `True` and `False` values by using `Vtrace < threshold`. Then, the entries of the array will be `True` whenever the voltage is below threshold. The time point of crossing the threshold is when a `False` entry is followed by a `True` entry. Use this information to determine the spike times and pass them to a numpy array called 'spikeTimes'.
# 
# Check if you really got the right spike timings by plotting them in a new plot together with the voltage trace.

# In[8]:

above = (Vtrace < threshold)
spikes = above[1:] < above[0:-1]
spikeTimes = tbins[spikes]
pl.plot(tbins, Vtrace, tbins[spikes], Vtrace[spikes], 'xr')
pl.xlim([0, 1])


# In[9]:

interval = np.arange(0, 4, 0.2)
psth = np.zeros([len(trigger), len(interval)-1])

for i in range(len(trigger)):
    psth[i, :] = np.histogram(spikeTimes - trigger[i], interval)[0]

print shape(np.repeat(interval, 2))
#pl.plot(np.repeat(interval, len(trigger)), psth)


#### b) Inter-spike-intervals and histograms

# Obtain the differences between spike times and pass them to the variable `ISI`.

# In[10]:

ISI = np.diff(spikeTimes)


# Plot these values into a histogram.

# In[48]:

ISIhist = pl.hist(ISI, 20)


### 5. Fitting (Poisson distribution, tuning curve?)

# In[51]:

p = np.polyfit(ISIhist[1][:-1], ISIhist[0], 3)
import scipy.optimize as opt
import scipy as sc

def poisson(x, a):
    y = x**a/sc.misc.factorial(a)*np.exp(-x)
    return y

print opt.curve_fit(poisson, ISIhist[1][:-1], ISIhist[0])
# ss.lognorm.fit(ISIhist[0]) # output: shape, location, scale


# In[ ]:




import numpy as np
import matplotlib.pyplot as pl

# convenience functions to unpack structures in mat-files
from loaddata import *

#=== Part 1 ===========================================================

# --- 1.
(I,FI,TimeResolutionS,SamplingFrequencyHz) = load1()

# --- 2.
samplesPerSec = SamplingFrequencyHz * 1 #sec
firstSample = 30000 # arbitrary
lastSample = firstSample + samplesPerSec

pl.figure()
pl.title('Cutout of I and FI')
pl.xlabel('Time (ms)')
pl.ylabel('PSC')

#plot only first second
tVals = np.linspace(firstSample*TimeResolutionS \
                    ,lastSample*TimeResolutionS \
                    ,samplesPerSec)
pl.plot(tVals, I[firstSample:lastSample],'b-',label='I')
pl.plot(tVals, FI[firstSample:lastSample],'g-',linewidth=2,label='FI')
pl.legend()

# --- 3.
thr = -20
cond = np.logical_and( FI[:-1]>=thr, FI[1:]<thr )
# as FI has shape (?,1), i.e. is a matrix np.nonzero return (x,y) values
# but we need only the first dimension
onset_idx = np.nonzero(cond)[0]
nPSCs = len(onset_idx)
print "Detected number of PSCs=", nPSCs

# mark onset_idx in plot
cond = np.logical_and(onset_idx>=firstSample, onset_idx<lastSample)
idxInPltRange = onset_idx[cond]
for i in idxInPltRange:
    pl.axvline(i*TimeResolutionS,color='r')

# --- 4.
nBefore = 200
nAfter  = 700
PSCs=np.zeros((nPSCs, nBefore+nAfter))
for i in np.arange(nPSCs):
    PSCs[i] = I[onset_idx[i]-nBefore:onset_idx[i]+nAfter].ravel()

# --- 5.

tVals = np.arange(-nBefore*TimeResolutionS \
                   ,nAfter*TimeResolutionS \
                   ,TimeResolutionS)
pl.figure()
pl.title('Spike-triggered PSC')
pl.xlabel('Time (ms)')
pl.ylabel('PSC')
pl.plot(tVals,PSCs.T)
avgPSC = PSCs.mean(axis=0)
pl.plot(tVals,avgPSC,'r', linewidth='2')


pl.figure()
pl.subplot(3,1,1)
pl.plot(tVals,avgPSC,'r', linewidth='2')
stdPSC = PSCs.std(axis=0)
pl.fill_between(tVals, avgPSC-stdPSC, avgPSC+stdPSC, color='y')

peakAmplitudeAvg = avgPSC.max()-avgPSC.min()
print 'Peak amplitude of average PSC:', peakAmplitudeAvg

# --- 6.
peakAmplitude = PSCs.max(axis=1)-PSCs.min(axis=1)
pl.subplot(3,1,2)
pl.hist(peakAmplitude,bins=20)
pl.subplot(3,1,3)
pl.hist(np.log(peakAmplitude),bins=20)

pl.title('Statistics')

# --- 7. Do all your graphs have proper axes labeling and units?
# to do

#=== Part 2 ===========================================================

# --- 1.
(I,Z,I_SamplingFrequencyHz,Z_SamplingFrequencyHz) = load2()

# --- 2.
thr = -1.98
cond = np.logical_and( Z[:-1]>=thr, Z[1:]<thr )
# as FI has shape (?,1), i.e. is a matrix np.nonzero return (x,y) values
# but we need only the first dimension
onset_idx = np.nonzero(cond)[0]
assert(len(onset_idx)==42)
onset_idx = onset_idx.reshape(3,14)

# --- 3.
# calculate stimulation times from onset indices
stim_times = onset_idx / Z_SamplingFrequencyHz
# calculate corresponding stimulation indices for current trace I
i_idx = np.round(stim_times * I_SamplingFrequencyHz)

nSamples = I_SamplingFrequencyHz * 0.1 # 0.1 sec
tVals = np.linspace(0,0.1,nSamples)

def ana(stimSite):
    nStimulationsPerSite = 14
    PSCs = np.zeros((nStimulationsPerSite, nSamples))
    for i in np.arange(nStimulationsPerSite):
        idx = i_idx[stimSite,i]
        PSCs[i,:] = I[idx:idx+nSamples]

    pl.figure()
    pl.title('')
    pl.xlabel('Time (ms)')
    pl.ylabel('PSC')
    pl.plot(tVals, PSCs.T)

    peakAmplitude = PSCs.max(axis=1)-PSCs.min(axis=1)
    meanAmp = peakAmplitude.mean(axis=0)
    stdAmp = peakAmplitude.std(axis=0)
    cv = stdAmp / meanAmp

    pl.text(0.06,-80,'mean=%g\nstd=%g\ncv=%g' % (meanAmp, stdAmp, cv))

    return (meanAmp, stdAmp, cv)

(meanAmp0, stdAmp0, cv0) = ana(0)
(meanAmp1, stdAmp1, cv1) = ana(1)
(meanAmp2, stdAmp2, cv2) = ana(2)

pl.figure()
pl.title('Temporal precision')
pl.xlabel('Delay (ms)')
pl.ylabel('Precision (ms)')
pl.plot( [meanAmp0, meanAmp1, meanAmp2], [cv0, cv1, cv2], 'o' )

# --- 4.
thr=-10
filter=np.exp( (np.arange(-0.03,0.03,1/I_SamplingFrequencyHz)/0.01)**2 )
filter /= filter.sum()
onset_times_thr = np.zeros(42)
for i in np.arange(42):
    idx = i_idx.ravel()[i]
    PSC = np.convolve(I[idx:idx+nSamples],filter,'same')
    dyn_thr = PSC.max() + thr
    cond = np.logical_and( PSC[:-1]>=dyn_thr, PSC[1:]<dyn_thr )
    onset_times_thr[i] = np.nonzero(cond)[0][0] / I_SamplingFrequencyHz

stim_std = onset_times_thr.std()
print "Std of stimulation times:", stim_std

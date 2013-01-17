#!/usr/bin/env python
from random import *
from math import *
MAX=80;

def histgram( data, numbins ):
    step = (max(data)-min(data))/numbins;
    midpts = [ min(data)+i*step+step/2 for i in range(numbins) ];
    h = [0 for i in range(numbins)];
    for d in data:
        idx = int(floor( (d-min(data))/(max(data)-min(data))*numbins ))
        h[idx if idx<numbins else numbins-1] +=1
    return (midpts,h)

def drawhistgram( h ):
    for i in range( len(h[0]) ):
        print "% 4.2f "%h[0][i], "*" * int((h[1][i]/float(max(h[1])))*MAX);


## testing
data=[normalvariate( mu=0, sigma=1 ) for i in range(500)];
z=histgram( data, 10 );
drawhistgram( z );

for i in range(5,50,5):
    print "\ni=%d"%i
    drawhistgram( histgram( data, i ) )


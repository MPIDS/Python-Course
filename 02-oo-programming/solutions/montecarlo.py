#!/usr/bin/env python

import random

def countsix( n, ndice=2 ):
    p=0;
    for i in range(n):
        p+=sum([random.randint( 1, 6 )==6 for i in range(ndice)])>0;
    return p

n=5000000; ndice=2;
print "11/36=%.4f"%(11.0/36)
print "sim  =%.4f"%(countsix(n,2)/float(n))

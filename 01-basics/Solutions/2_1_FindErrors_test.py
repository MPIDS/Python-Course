#!/usr/bin/env python
import sys, random

def compute(n):
    i = 1; s = 0
    while i <= n:
        s += random.random()
        print(s)
        i += 1
    return s/n

n = int(sys.argv[1])
print 'the average of %d random numbers is %g' % (n, compute(n))
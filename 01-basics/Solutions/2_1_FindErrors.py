#!/usr/bin/env python3

import sys, random

print("TEST", sys.argv)

print(sys.argv[10])

def compute(n):
    i = 0; s = 0
    while i < n:
        s += random.random()
        i += 1
    return s/n

n = int(sys.argv[1])
print('the average of %d random numbers is %g' % (n, compute(n)))

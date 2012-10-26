#!/usr/bin/env python
from math import *

def pol2cart( pts ):
    if isinstance( pts, tuple ):
        pts=[pts];
    c=[ (r*cos(th), r*sin(th)) for (r,th) in pts ];
    return c if len(c)>1 else c[0]

def cart2pol( pts ):
    if isinstance( pts, tuple ):
        pts=[pts];
    p=[ (sqrt(x**2+y**2), atan(float(y)/x)) for (x,y) in pts ];
    return p if len(p)>1 else p[0]


pts=[(2,1), (3.4, 5.3)];
print "Cartesian : ",pts
print "Polar     : ",cart2pol( pts );
print "And Back  : ",pol2cart(cart2pol( pts ));

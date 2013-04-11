import meanrand
import pylab as pl
import time,random

meanrand.setseed(324)

def meanrand_python(n):
    i=0
    res=0.0
    while i<n:
        res+=random.random()
        i+=1
    return res/n

rt_c=[]
rt_python=[]
ns=[10**i for i in range(8)]
for i in ns:
    start=time.time()
    meanrand.meanrand(i)
    rt_c.append(time.time()-start)

    start=time.time()
    meanrand_python(i)
    rt_python.append(time.time()-start)

pl.semilogx( ns, rt_c, ".-", label="C", linewidth=3 )
pl.semilogx( ns, rt_python, ".-", label="Python",linewidth=3 )
pl.xlabel("num runs")
pl.ylabel("runtime")
pl.legend()
pl.show()

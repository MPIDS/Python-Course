import numpy as np
import mlpy.dtwcore as md
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dt=0.7
xr=np.arange(0,4*np.pi,dt)
x = np.sin(xr)
y = np.sin((xr+1*np.pi)*.5)
dist, p1, p2, cost = md.dtw(x, y)

cost.tofile("costmatrix.csv", sep=",")

X = np.arange(0,len(x))
Y = np.arange(0,len(y))
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, cost, rstride=1, cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)

ax.plot( p2, p1, cost[p1,p2], color="red", linewidth=4 )
plt.show()


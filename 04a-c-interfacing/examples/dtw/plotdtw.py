import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plotdtw( D, p ):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    (N1,N2)=D.shape
    X = np.arange(0,N1)
    Y = np.arange(0,N2)
    X, Y = np.meshgrid(X, Y)

    surf = ax.plot_surface(X, Y, D, rstride=1, cstride=1, cmap=cm.jet,
                           linewidth=0, antialiased=False)

    p1=p[0,:]
    p2=p[1,:]
    ax.plot( p2, p1, D[p1,p2], color="red", linewidth=4 )
    plt.show()



def mysurf( D ):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    (N1,N2)=D.shape
    X = np.arange(0,N1)
    Y = np.arange(0,N2)
    X, Y = np.meshgrid(X, Y)

    surf = ax.plot_surface(X, Y, D, rstride=1, cstride=1, cmap=cm.jet,
                           linewidth=0, antialiased=False)
    
    plt.show()

def getexamplematrix( dt ):
    xr=np.arange(0,4*np.pi,dt)
    x = np.sin(xr)
    y = np.sin((xr+1*np.pi)*.5)
    D=np.zeros( (len(x), len(y)) )
    for i in range(len(x)):
        for j in range(len(y)):
            D[i,j]=(x[i]-y[j])**2
    return D
      
                

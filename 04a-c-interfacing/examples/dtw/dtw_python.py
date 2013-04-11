import numpy as np
import math

def dtw( M ):
    """Given a matrix M, calculate the shortest path between (0,0) and (N1,N2)"""
    N1,N2=M.shape
    D=M.copy()
    for i in range(N1-1):
        for j in range(N2-1):
            D[i+1,j+1]=M[i,j]+min([D[i,j+1],D[i+1,j],D[i+1,j+1]])

    p1,p2=([N1-1],[N2-1])
    while p1[0]>0 or p2[0]>0:
        i,j=(p1[0],p2[0]) 
        midx=np.argmin( np.array( \
            [ D[i-1,j  ] if i>0 else np.inf, \
              D[i,j-1  ] if j>0 else np.inf, \
              D[i-1,j-1] if i>0 and j>0 else np.inf]))
        if midx==0:
            p1.insert(0,i-1)
            p2.insert(0,j  )
        elif midx==1:
            p1.insert(0,i  )
            p2.insert(0,j-1)
        else:
            p1.insert(0,i-1)
            p2.insert(0,j-1)
            
    return D,np.array([p1,p2])


if __name__=='__main__':
    M=np.fromfile("costmatrix.csv",sep=",")
    N=int(math.sqrt(M.size))
    M.shape=(N,N)

    D,p= dtw(M)

    from  plotdtw import *
    plotdtw(M,p)

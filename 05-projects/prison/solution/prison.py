#!/usr/bin/env python

import numpy as np
import pylab as pl
import random

# 0,False - cooperate
# 1,True  - defect
payoff = np.array([ [7, 0], [10, 0] ]); # from Grujic et al (2010)

# grid size
N=40;

# player's strategies
num2strat={ 1:lambda s,o: random.randint( 0,1),                   # random
            2:lambda s,o: np.argmax( np.array([np.sum(s==0),np.sum(s==1)]) ), # tit-for-tat, 50 percent
            3:lambda s,o: s[np.argmax(o)] }                       # imitate the best

def getneighbours( M, i, j ):
    """
    returns the 8 neighbours of i,j from matrix M with
    continuous boundary conditions as numpy array
    """
    nh=np.tile(0,8); (ml,mc)=M.shape;
    idx = lambda i,add,l: i+add if (i+add>=0 and i+add<l) else l-1 if i+add<0 else 0;
    index=0;
    for ix in [-1,0,1]:
        for jx in [-1,0,1]:
            if ix==jx==0: continue
            nh[index]=M[ idx(i,ix,ml), idx(j,jx,mc) ];
            index+=1
    return (nh.astype(int));

def prison_run( initial, strat, nruns ):
    """
    - initial holds the initial choice of strategy
    - strat   holds numbers symbolizing the strategy (mapped by num2strat)
    - nruns   is the number of iterations
    """
    S = np.zeros( (N,N,nruns),dtype=np.int ); # strategy array
    P = np.zeros( (N,N,nruns),dtype=np.int ); # payoff   array 
    S[:,:,0]=initial;
    for t in range(nruns-1):
        for i in range(N):
            for j in range(N):
                nh = getneighbours(S[:,:,t],i,j); # get neighbour strategies
                P[i,j,t  ]=np.sum( payoff[ np.zeros(8,dtype=np.int)+S[i,j,t], nh ] );
                no = getneighbours(P[:,:,t],i,j); # get neighbour payoffs
                S[i,j,t+1]=(num2strat[strat[i,j]])( nh, no )

    return (S,P);



initial = np.array([random.sample([True,False],1) for i in range(N*N)]).reshape(N,N); # random initial strategies
strat = np.zeros( (N,N), dtype=np.int)+2; # only random players
(S,P) = prison_run( initial, strat, 100 );


pl.ion()
for i in range(100):
    pl.imshow( S[:,:,i] );
    raw_input("Press Enter to continue...")
pl.ioff() 

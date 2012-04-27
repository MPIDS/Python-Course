from pylab import *
from numpy import *
from scipy import *
from scipy.integrate import *

## plot a 1D gauss with mean 10 and sd=5
ion()
figure(1)
x=arange(0,20,0.01);
mu=16;
sigma=5;
def gauss( x, mu, sigma):
    return 1/(sqrt(2*pi)*sigma) * exp( -(x-mu)**2/(2*sigma**2) );
plot( x, gauss( x, mu, sigma ) );

## integrate the gauss on the interval of mu-50 and mu+50 and verify that it is equal to 1
figure(2)
data = []
for win in arange(0,25,0.1):
    data.append([win,  quad( gauss, mu-win, mu+win, args=(mu,sigma) )[0]])
data=array(data)
plot(data[:,0], data[:,1])
    
## plot a 2D standardnormal distribution
figure(3)

y = x = arange(-3,3,0.01)
X,Y = meshgrid(x,y)

Z = 1/(sqrt(2*pi)) *exp ( - (X**2 +  Y**2)/2 )

contour(X,Y,Z)
imshow(Z)
colorbar()


## rearrange gaussian 
(n,n)=Z.shape

Z2 = empty (Z.shape)

Z2[:n/2,:n/2] = Z[n/2:, n/2:]
Z2[n/2:,:n/2] = Z[:n/2, n/2:]
Z2[n/2:,n/2:] = Z[:n/2, :n/2]
Z2[:n/2,n/2:] = Z[n/2:, :n/2]

figure(4)
imshow(Z2)
colorbar()

figure(5)
imshow(Z-Z2)
colorbar()

## monte-carlo, vectorized version
figure(6)
Ns=arange(1000,100000,1000);
R=[];
for N in Ns:
    R.append(sum(sum((random.randint(1,7,(N,2))==6), 1)>0)/float(N))

plot( Ns, R );
semilogx( Ns, R );


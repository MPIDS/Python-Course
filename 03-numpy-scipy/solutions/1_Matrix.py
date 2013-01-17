import numpy as np

# (a)
data = np.ones((4,4))
data[3,1]=6
data[2,3]=2
print data

data =  np.diag(range(1,7))[:,1:]
print data


# (b)
print np.arange(1,16).reshape(3,5).T

# (c)
a = np.arange(25).reshape(5,5)
b = np.array( [1., 5., 10., 15., 20.] )

print a
a = np.array (a, dtype = float) 
print a 
for i in range( a.shape[0]):
  a[:,i] /= b
print a

# or in one line

a = np.arange(25).reshape(5,5)
print (a.T/b ).T
# (d)
data = np.random.rand ( 10, 3)
j=abs(data-0.5).argsort()[:,0]
i= range(10)

print data
print data[i,j]


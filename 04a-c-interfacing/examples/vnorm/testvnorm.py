import vnorm, numpy, math, scipy.linalg

python_vnorm=lambda seq: math.sqrt(sum([x**2 for x in seq]))

tests=[ numpy.random.rand(1000),\
        [1,3,4,5],\
        (1,10,100,1000) ]

for test in tests:
    print vnorm.vnorm( test ), python_vnorm( test ), scipy.linalg.norm(test)

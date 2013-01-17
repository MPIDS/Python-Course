# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def f():
    count = 0
    for i in range(1000000):
        if i%7 == 0:
            count += 1
    return count
%timeit f()

# <codecell>

%timeit len([x for x in range(1000000) if x%7 == 0])

# <codecell>

import numpy as np
%timeit np.sum(np.mod(np.arange(1000000), 7) == 0)


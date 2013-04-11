import geomean
import numpy as np
import scipy.stats as stats
import pylab as pl

ns=[10**i for i in range(8)]
pl.semilogx( ns, [geomean.geomean_pow(np.random.rand(i)) for i in ns], color="red", label="pow", linewidth=3)
pl.semilogx( ns, [geomean.geomean_ln(np.random.rand(i)) for i in ns], color="blue", label="ln", linewidth=3)
pl.semilogx( ns, [stats.gmean(np.random.rand(i)) for i in ns], color="orange", label="scipy", linewidth=3)
pl.legend()
pl.xlabel("num samples")
pl.ylabel("GM(x)")
pl.show()

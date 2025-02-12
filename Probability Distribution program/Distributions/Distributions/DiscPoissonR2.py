# poisson application
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
lambd=5
x = np.arange(0,11)
rv = stats.poisson(lambd)
f = rv.pmf(x)
r = np.cumsum(f)
plt.step(x,r,color='b')
plt.step(x-1,r, 'bo', lw=5 ,color='b')
plt.title("CDF")
plt.show()
plt.plot(x, f, 'bo', ms =8 ,color='b' )
plt.vlines(x,0,f,color = 'b', lw = 5)
plt.xlabel("number of orders arrive per day")
plt.ylabel("probability")
plt.title("PMF")
plt.show()
pass
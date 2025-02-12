# poisson approximation to binomial
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def discrete_poisson(n, p):
    lambd = 5
    n = 10000
    p = 0.01
    y = np.arange(0,150)
    rv2 = stats.poisson(n*p)
    f = rv2.pmf(y)
    r = np.cumsum(f)
    plt.step(y,r)
    plt.step(y,r, 'bo', ms = 0.5)
    plt.title("CDF")
    plt.show()
    plt.plot(y,f,'bo', ms=5, label="binomial",color='b' )
    plt.vlines(y, 0, f, color='b', lw=0.9)
    plt.plot(f, color='r', label="poisson")
    plt.legend()
    plt.xlabel("number of errors introduced by the channel ")
    plt.ylabel("probability")
    plt.title("PMF")
    plt.show()
    print("expectation = ", lambd)
    print("variance = ", lambd)
pass



import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def continuous_uniform(a, b):
    rand_unif = stats.uniform.rvs(loc=a, scale=(b-a), size=1000)

    #PDf  for Uniform
    plt.ylim(-0.01, 1.5)
    plt.xlim(0, b+5)
    plt.title("PDf for Uniform distribution ", fontsize =16)
    plt.ylabel("Probability", fontsize =14)
    plt.xlabel("x", fontsize =14)
    x = np.arange(0, b+5, 0.001)
    plt.plot(x, stats.uniform.pdf(x, loc=a, scale=(b-a)), color="darkblue")
    plt.show()

    #CDf  for Uniform
    plt.ylim(-0.01, 1.5)
    plt.xlim(0, b+5)
    plt.title("CDF for Uniform distribution ", fontsize =16)
    plt.plot(x, stats.uniform.cdf(x, loc=a, scale=(b-a)), color="darkblue")
    plt.xlabel("x", fontsize =14)
    plt.ylabel("Probability", fontsize =14)
    plt.show()

    M = np.mean(rand_unif )
    V = np.var(rand_unif )
    print("Mean= ",M)
    print("variance= ",V)
pass
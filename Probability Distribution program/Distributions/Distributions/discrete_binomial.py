import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
def discrete_binomial(n, p):
    # Set the number of trials and probability of success
    n = 10
    p = 0.3

    # Generate the random variable
    rv = binom(n, p)
    print(f'Number of trials: {n}')
    print(f'Random variable value: {rv.rvs()}')

    # Plot the PMF
    x = np.arange(rv.ppf(0.01), rv.ppf(0.99))
    plt.plot(x, rv.pmf(x), 'bo', ms=8, label='binom pmf')
    plt.vlines(x, 0, rv.pmf(x), colors='b', lw=5, alpha=0.5)
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.title('Binomial PMF')
    plt.show()

    # Plot the CDF
    x = np.arange(rv.ppf(0.01), rv.ppf(0.99))
    plt.step(x,rv.cdf(x), color='b')
    #plt.vlines(x, 0, rv.cdf(x), colors='b', lw=1.5)
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.title('Binomial CDF')
    plt.show()

    # Compute the expectation and variance
    print(f'Expectation: {rv.mean()}')
    print(f'Variance: {rv.var()}')
pass
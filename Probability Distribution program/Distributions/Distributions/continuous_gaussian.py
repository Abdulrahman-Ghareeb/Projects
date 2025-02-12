import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def continuous_gaussian(mean, std, sample_size=10000):
    # Set the mean and standard deviation of the Gaussian distribution
    mean = 0
    std = 1

    # Generate random samples from the Gaussian distribution
    samples = np.random.normal(mean, std, size=10000)

    # Plot the PMF of the samples
    plt.hist(samples, bins=50, density=True, alpha=0.5)
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('PMF of Gaussian Continuous Random Variable')
    plt.show()

    # Plot the PDF of the samples
    x = np.linspace(-5, 5, 100)
    plt.plot(x, norm.pdf(x, mean, std))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('PDF of Gaussian Continuous Random Variable')
    plt.show()

    # Plot the CDF of the samples
    plt.hist(samples, bins=50, density=True, alpha=0.5, cumulative=True)
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('CDF of Gaussian Continuous Random Variable')
    plt.show()

    # Calculate the expectation of the samples
    expectation = np.mean(samples)
    print(f'Expectation: {expectation}')

    # Calculate the variance of the samples
    variance = np.var(samples)
    print(f'Variance: {variance}')
pass

import matplotlib.pyplot as plt
import numpy as np
def continuous_exponential(lambda_=0.1, n=1000):
    # Rate parameter for the exponential random variable
    lambda_ = 0.1

    # Number of random variables to generate
    n = 1000

    # Generate n exponential random variables

    x = np.random.exponential(1 / lambda_, n)
    #np.random.exponential(scale, size): This function generates random numbers from an exponential distribution

    x = x[(x > 10) & (x <= 15)]  # Filter values between 10 and 15


    # Compute the probability density function (PDF)
    x_min, x_max = min(x), max(x)
    bins = np.linspace(x_min, x_max, 50) #This line creates 50 evenly spaced bins & (np.linspace) is used to generate these bins.

    pdf, _ = np.histogram(x, bins=bins, density=True)
    #This line calculates the histogram of the data &&density=True parameter means that the area under the histogram will sum up to 1,


    # Compute the cumulative distribution function (CDF)
    cdf = np.cumsum(pdf * np.diff(bins))
    #you're essentially summing up the areas of each histogram bin (calculated from the PDF)
    #and accumulating these values to generate the cumulative distribution function (CDF)


    # Compute the expectation of the exponential random variable
    expectation = 1 / lambda_

    # Compute the variance of the exponential random variable
    variance = (1 / lambda_) **2

    # Plot the PDF using fill_between
    plt.fill_between(bins[:-1], pdf, 0)
    plt.title('Probability Density Function (PDF)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

    # Plot the CDF
    plt.plot(bins[:-1], cdf, 'o-')
    plt.title('Cumulative Distribution Function (CDF)')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.show()

    # Print the results
    print(f'Expectation: {expectation:.2f}')
    print(f'Variance: {variance:.2f}')
pass

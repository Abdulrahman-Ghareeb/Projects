import numpy as np
import matplotlib.pyplot as plt
def discrete_uniform(a, b):
    # Set the range of the random variable
    # Change 'b' to set the upper limit (inclusive) of the range

    # Generate the random variable
    X = np.random.randint(a, b + 1, size=10000000)

    # Plot the PMF
    counts, bins, _ =plt.hist(X, bins=np.arange(a - 0.5, b + 1.5), density=True,rwidth=0.2,edgecolor="black",linewidth=0.5)
    plt.xticks(np.arange(a,b+1,1))
    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.title("Probability Mass Function of Uniform Discrete Random Variable")
    bar_centers = bins[:-1] + 0.5
    plt.scatter(bar_centers, counts, s=60, color='red', zorder=5)
    plt.show()



    # Plot the CDF
    counts, bins, _ = plt.hist(X, bins=np.arange(a - 0.5, b + 1.5), density=True,cumulative=True,label='CDF')
    plt.plot(bins[:-1], counts, "o-", color='red')
    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.title("Cumulative Distribution Function of Uniform Discrete Random Variable")
    plt.show()

    # Compute the expectation and variance
    expectation = (a + b) / 2
    variance = ((b - a + 1) ** 2 - 1) / 12
    print("Expectation:", expectation)
    print("Variance:", variance)
pass
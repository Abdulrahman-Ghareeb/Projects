import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
def discrete_geometric(prob_success_input, num_variables_input, k_trials=10):
    def generate_geometric_random_variables(prob_success, size=1):

        # Checking the probability range
        if prob_success <= 0 or prob_success > 1:
            raise ValueError("Probability of success must be in the range (0, 1].")

        # Generating geometric random variables
        geometric_values = np.random.geometric(p=prob_success, size=size)

        return geometric_values

    def geometric_pmf(p, k):

        pmf = {(1 + i): p * (1 - p)**i for i in range(k)}
        return pmf

    def geometric_cdf(p, k):

        pmf = geometric_pmf(p, k)
        cdf = {key: sum(pmf[i] for i in range(1, key+1)) for key in pmf}
        return cdf

    def calculate_statistics(pmf):

        e_x = sum(value * probability for value, probability in pmf.items())
        e_x_squared = sum(value**2 * probability for value, probability in pmf.items())
        var_x = e_x_squared - e_x**2
        return e_x, e_x_squared, var_x

    def plot_geometric_distribution(prob_success, size=1000):
        # Generate random variables
        random_variables = generate_geometric_random_variables(prob_success, size)

        # Calculate the probability mass function (PMF) and cumulative distribution function (CDF)
        x = np.arange(1, np.max(random_variables) + 1)
        pmf = geom.pmf(x, p=prob_success)
        cdf = geom.cdf(x, p=prob_success)


        # Plot PMF on the left subplot

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.stem(x, pmf, basefmt="b", linefmt="b-", markerfmt="bo", label='PMF')
        plt.title('Geometric Distribution - Probability Mass Function')
        plt.xlabel('Number of Trials until Success')
        plt.ylabel('Probability')
        plt.legend()

        # Plot CDF on the right subplot
        plt.subplot(1, 2, 2)
        plt.step(x, cdf, color='green', label='CDF')
        plt.title('Geometric Distribution - Cumulative Distribution Function')
        plt.xlabel('Number of Trials until Success')
        plt.ylabel('Cumulative Probability')
        plt.legend()

        plt.tight_layout()
        plt.show()

    # Input probability of success
    prob_success_input = float(input("Enter the probability of success (0 < prob_success <= 1): "))

    # Input number of random variables to generate
    num_variables_input = int(input("Enter the number of random variables to generate: "))

    # Set the number of trials (you can adjust this based on your needs)
    k_trials = 10

    p_success = prob_success_input
    pmf = geometric_pmf(p_success, k_trials)
    cdf = geometric_cdf(p_success, k_trials)

    # Calculate statistics
    expected_value, expected_value_squared, variance = calculate_statistics(pmf)

    # Print statistics
    print("Probability Mass Function (PMF):", pmf)
    print("Cumulative Distribution Function (CDF):", cdf)
    print("Expected Value (E(X)): {:.2f}".format(expected_value))
    print("Expected Value of X^2 (E(X^2)): {:.2f}".format(expected_value_squared))
    print("Variance (Var(X)): {:.2f}".format(variance))
    # Plot the Geometric Distribution (PMF and CDF)
    plot_geometric_distribution(prob_success_input, size=num_variables_input)
pass
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
def discrete_bernoulli(p_success, num_patients):
    # Set the probability of success for the treatment
    p_success = 0.8  # You can adjust this probability based on your scenario

    # Number of patients
    num_patients = 1000

    # Generate synthetic data using Bernoulli distribution
    treatment_outcomes = bernoulli.rvs(p_success, size=num_patients)

    # Calculate success and failure counts
    success_count = np.sum(treatment_outcomes == 1)
    failure_count = np.sum(treatment_outcomes == 0)

    # Calculate expectation (mean) and variance
    expectation = p_success
    variance = p_success * (1 - p_success)

    # Display the results
    print(f"Success Count: {success_count}")
    print(f"Failure Count: {failure_count}")
    print(f"Expectation (Mean): {expectation}")
    print(f"Variance: {variance}")

    # Plot the distribution
    plt.bar(['Success', 'Failure'], [success_count, failure_count])
    plt.title('Distribution of Treatment Outcomes')
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.show()
pass
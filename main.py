import random
import math
import matplotlib.pyplot as plt

# Function to estimate pi using Monte Carlo simulation
def return_estimate(n_samples):
    num_inside = 0

    for i in range(n_samples):
        # Generate a random point between 0 and 1 for x.
        x = random.random()

        # Generate a random point between 0 and 1 for y.
        y = random.random()

        # Calculate the radius of this point.
        r = math.sqrt(x ** 2 + y ** 2)

        # Check if the point is inside the circle
        if r < 1:
            num_inside += 1

    # Calculate pi estimate
    estimate = 4 * num_inside / n_samples

    return estimate

# List of sample sizes for which we want to estimate pi
result_list = [10 ** i for i in range(1, 7)]

# Store the results and percent errors
pi_estimates = []
percent_errors = []

# Loop over each sample size
for n_samples in result_list:
    estimate = return_estimate(n_samples)
    pi_estimates.append(estimate)

    # Calculate the percent error
    percent_error = 100 * math.fabs(estimate - math.pi) / math.pi
    percent_errors.append(percent_error)

    print(f"{n_samples} samples: Estimated Pi = {estimate}, Percent Error = {percent_error:.2f}%")

# Plot the percent errors
plt.plot(result_list, percent_errors, 'bo-')

# Add labels and title
plt.xlabel("Number of Samples")
plt.ylabel("Percent Error (%)")
plt.title("Monte Carlo Pi Estimation - Percent Error")

plt.xscale('log')

# Show the plot
plt.show()
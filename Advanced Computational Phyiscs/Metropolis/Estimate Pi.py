import random
import numpy as np

def estimate_pi(N):
    count = 0
    for _ in range(N):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            count += 1
    pi = 4 * count / N
    return pi

total_iterations = 10**7
pi_estimate = estimate_pi(total_iterations)
print("Estimated value of pi:", pi_estimate)
print("real value:",np.pi)


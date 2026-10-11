import numpy as np
import matplotlib.pyplot as plt

def probability_distribution(x):
    return (np.abs(np.sin(x**2 + x**(-1/2) - 1)) + 0.5) / np.sqrt(x)

def metropolis_algorithm(N, proposal_width=0.1):
    x = np.random.uniform(0, np.pi)  
    samples = []
    for _ in range(N):
        x_new = x + np.random.uniform(-proposal_width, proposal_width)  
        if x_new < 0 or x_new > np.pi:
            continue  
        acceptance_probability = min(1, probability_distribution(x_new) / probability_distribution(x))
        if np.random.uniform(0, 1) < acceptance_probability:
            x = x_new  
        samples.append(x)
    return samples

N = 1000000
random_numbers = metropolis_algorithm(N)

plt.hist(random_numbers, bins=50, density=True)
x = np.linspace(0, np.pi, 1000)
y = probability_distribution(x)
plt.plot(x, y, color='red', lw=2)
plt.xlabel('Generated Numbers')
plt.ylabel('Probability Density')
plt.title('Distribution of Generated Numbers')
plt.show()

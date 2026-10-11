import numpy as np
import matplotlib.pyplot as plt

def probability_distribution(x):
    return np.abs(np.sin(x**2 + x**(1/2) - 1))

def generate_random_numbers(N):
    random_numbers = []
    while len(random_numbers) < N:
        x = np.random.uniform(0, np.pi)  
        y = np.random.uniform(0, 1)  
        if y <= probability_distribution(x):
            random_numbers.append(x)
    return random_numbers

N = 1000000
random_numbers = generate_random_numbers(N)

plt.hist(random_numbers, bins=50, density=True)
x = np.linspace(0, np.pi, 1000)
y = probability_distribution(x)
plt.plot(x, y, color='red', lw=2)
plt.xlabel('Generated Numbers')
plt.ylabel('Probability Density')
plt.title('Distribution of Generated Numbers')
plt.show()
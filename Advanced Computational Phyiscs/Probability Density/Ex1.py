import numpy as np
import matplotlib.pyplot as plt

def probability_distribution(x):
    return 1 / (x ** 3)

def generate_random_numbers(N):
    random_numbers = []
    while len(random_numbers) < N:
        x = np.random.uniform(1, 10)  
        y = np.random.uniform(0, 1 / 10) 
        if y <= probability_distribution(x):
            random_numbers.append(x)
    return random_numbers

N = 1000000
random_numbers = generate_random_numbers(N)

plt.hist(random_numbers, bins=50, density=True)
x = np.linspace(1, max(random_numbers), 1000)
y = probability_distribution(x)
plt.plot(x, y, color='red', lw=2)
plt.xlabel('Generated Numbers')
plt.ylabel('Probability Density')
plt.title('Distribution of Generated Numbers')
plt.show()
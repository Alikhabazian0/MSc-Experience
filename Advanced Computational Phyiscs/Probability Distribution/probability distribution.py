import numpy as np
import matplotlib.pyplot as plt

def probability_distribution(x):
    return np.exp(-x)

np.random.seed(0)
random_numbers = np.random.uniform(0, 1, size=1000)  
generated_numbers = -np.log(random_numbers) 

plt.hist(generated_numbers, bins=50, density=True, alpha=0.6, label='Generated Numbers')
x = np.linspace(0, 6, 100)
y = probability_distribution(x)
plt.plot(x, y, color='red', lw=2, label='p(x) = e^(-x)')
plt.xlabel('Generated Numbers')
plt.ylabel('Probability Density')
plt.title('Distribution of Generated Numbers')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def pdf(x):
    return np.sin((x ** 2) / 100) + 1 / np.cos((x ** 3) / 100) + x ** -3

def von_neumann_sampling(pdf, num_samples, x_min, x_max):
    samples = []
    while len(samples) < num_samples:
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(0, max_pdf)
        if y <= pdf(x):
            samples.append(x)
    return samples

num_samples = 10000
x_min = 1
x_max = 5

x_values = np.linspace(x_min, x_max, 1000)
pdf_values = pdf(x_values)
max_pdf = np.max(pdf_values)

samples = von_neumann_sampling(pdf, num_samples, x_min, x_max)

plt.figure(figsize=(8, 6))
plt.hist(samples, bins='auto', density=True, alpha=0.5, label='Generated Data')
plt.plot(x_values, pdf_values / max_pdf, 'r-', label='PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Von Neumann Sampling')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

sigma_0 = np.sqrt(2)
mean = 3
num_samples = 10000

u1 = np.random.uniform(size=num_samples)
u2 = np.random.uniform(size=num_samples)

r = np.sqrt(-2 * np.log(u1))
theta = 2 * np.pi * u2

x = mean + sigma_0 * r * np.cos(theta)

hist, bins = np.histogram(x, bins='auto', density=True)

bin_centers = (bins[:-1] + bins[1:]) / 2

popt, _ = curve_fit(gaussian, bin_centers, hist, p0=[mean, sigma_0])

pdf_fit = gaussian(bin_centers, *popt)

plt.figure(figsize=(8, 6))
plt.hist(x, bins='auto', density=True, alpha=0.5, label='Generated Data')
plt.plot(bin_centers, pdf_fit, 'r-', label='Gaussian Fit')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Gaussian Random Field Generation and PDF Fitting')
plt.legend()
plt.show()
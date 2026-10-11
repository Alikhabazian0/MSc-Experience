"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
def generate_gaussian_numbers(mean, std, num_samples):
  u1 = np.random.uniform(0 , 1, num_samples)
  u2 = np.random.uniform(0 , 1, num_samples)
 
  z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
  z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
 
  x = mean + std * z1
  y = mean + std * z2
 
  return x, y
 
mean = 1
std = 2
num_samples = 1000000
 
x, y = generate_gaussian_numbers(mean, std, num_samples)

# Plotting the histogram
plt.hist(x, bins=50, density=True, alpha=0.7, label='x')
plt.hist(y, bins=50, density=True, alpha=0.7, label='y')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Gaussian Random Numbers')
plt.show()

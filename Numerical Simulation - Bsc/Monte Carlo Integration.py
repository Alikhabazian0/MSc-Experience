"""
 Auther: Ali khabazian
 computational physics, physics group, IUST
 created on july 2023
"""
import numpy as np

def f(x, y):
    a = 0
    b = 0
    return np.sin(a * x + np.pi/4) * np.cos(b * x) * (a * y**2 + b**2 * x + 1)**(1/2)

def monte_carlo_integration(func, a, b, num_samples):
    integral_sum = 0.0

    for _ in range(num_samples):
        x = np.random.uniform(a[0], a[1])
        y = np.random.uniform(b[0], b[1])
        integral_sum += func(x, y)

    area = (a[1] - a[0]) * (b[1] - b[0])
    integral_approximation = (1 / num_samples) * integral_sum * area

    return integral_approximation

a = [np.pi/2, 0]  # Limits for x
b = [np.pi/2, 0]  # Limits for y
num_samples = 1000000

result = monte_carlo_integration(f, a, b, num_samples)
print("Approximate integral:", result)

#...........................................................................................
import numpy as np
from math import sqrt
def f(x, y, a, b):
    return np.sin(a * x + np.pi/4) * np.cos(b * x) * sqrt(a * y**2 + b**2 * x + 1)
 
def monte_carlo_integration(func, a, b, num_samples):
     integral_sum = 0.0
 
     for _ in range(num_samples):
        x = np.random.uniform(a[0], a[1])
        y = np.random.uniform(b[0], b[1])
        integral_sum += func(x, y, a[2], b[2])
 
     area = (a[1] - a[0]) * (b[1] - b[0])
     integral_approximation = (1 / num_samples) * integral_sum * area
 
     return integral_approximation
 
a = [np.pi/2, 0, 2]  # Limits for x and value of a
b = [np.pi/2, 0, 3]  # Limits for y and value of b
num_samples = 1000000
 
result = monte_carlo_integration(f, a, b, num_samples)
print("part 2:", result)

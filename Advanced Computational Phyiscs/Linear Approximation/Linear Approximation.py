import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Define the function f(x) = sin(x^2)
def f(x):
    return np.sin(x**2)

# a) Choose 30 points randomly and get f(i)
np.random.seed(42)
x_values = np.sort(np.random.uniform(0, 3, 30))
y_values = f(x_values)

# Calculate f(x) for linear approximations and Lagrange polynomial approximations
x_interp = np.linspace(0, 3, 1000)  # Interpolation points
linear_approximation = np.interp(x_interp, x_values, y_values)
lagrange_approximations = []

# Calculate Lagrange polynomial approximations for 1, 2, 4, 8, 16, 29 terms
for n in [1, 2, 4, 8, 16, 29]:
    lagrange_poly = lagrange(x_values[:n], y_values[:n])
    lagrange_approx = lagrange_poly(x_interp)
    lagrange_approximations.append(lagrange_approx)

# b) Draw the function for 30 points at a distance of 0.03
x_dense = np.arange(0, 3, 0.03)
y_dense = f(x_dense)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_interp, linear_approximation, label="Linear Approximation")
for i, n in enumerate([1, 2, 4, 8, 16, 29]):
    plt.plot(x_interp, lagrange_approximations[i], label=f"Lagrange ({n} terms)")
plt.legend()
plt.title("Approximations of f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")

# c) Consider 5 random points between [0,1] as noise and draw its graph
x_noise = np.sort(np.random.uniform(0, 1, 5))
y_noise = np.random.uniform(-0.5, 0.5, 5)
x_with_noise = np.concatenate((x_values, x_noise))
y_with_noise = np.concatenate((y_values, y_noise))

plt.subplot(1, 2, 2)
plt.plot(x_with_noise, y_with_noise, 'o', label="Data with Noise")
plt.plot(x_interp, linear_approximation, label="Linear Approximation")
for i, n in enumerate([1, 2, 4, 8, 16, 29]):
    plt.plot(x_interp, lagrange_approximations[i], label=f"Lagrange ({n} terms)")
plt.legend()
plt.title("Approximations of f(x) with Noise")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.tight_layout()
plt.show()

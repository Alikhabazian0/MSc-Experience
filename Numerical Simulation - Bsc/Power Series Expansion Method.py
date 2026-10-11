"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

def potential(x, a, l):
    if np.abs(x) <= l:
        return a * x**2
    else:
        return np.inf

def power_series_expansion_method(a, l, num_terms):
    def equation(x, y):
        return 2 * (a * x**2) * y

    x_start = -l
    x_end = l
    num_points = 1000
    x_values = np.linspace(x_start, x_end, num_points)
    dx = x_values[1] - x_values[0]
    y_values = np.zeros_like(x_values)

    for i, x in enumerate(x_values):
        y = np.zeros(num_terms)
        y[0] = 1.0  # Set the initial term in the expansion

        for j in range(1, num_terms):
            y[j] = (-equation(x, y[j-1]) * (x - x_start)**j) / (j * (j + 1))

        y_values[i] = np.sum(y)

    energy_values = 0.5 * y_values**2  # Calculate the energies

    return energy_values

a= 0
l = 1
num_terms = 10

# Using power series expansion method
power_series_energies = power_series_expansion_method(a, l, num_terms)
min_energy_power_series = np.min(power_series_energies)
max_energy_power_series = np.max(power_series_energies)

print("Power Series Expansion Method:")
print("Minimum Energy:", min_energy_power_series)
print("Maximum Energy:", max_energy_power_series)

#...........................................................
import numpy as np

def potential(x, a, l):
    if np.abs(x) <= l:
        return a * x**2
    else:
        return np.inf

def power_series_expansion_method(a, l, num_terms):
    def equation(x, y):
        return 2 * (a * x**2) * y

    x_start = -l
    x_end = l
    num_points = 1000
    x_values = np.linspace(x_start, x_end, num_points)
    dx = x_values[1] - x_values[0]
    y_values = np.zeros_like(x_values)

    for i, x in enumerate(x_values):
        y = np.zeros(num_terms)
        y[0] = 1.0  # Set the initial term in the expansion

        for j in range(1, num_terms):
            y[j] = (-equation(x, y[j-1]) * (x - x_start)**j) / (j * (j + 1))

        y_values[i] = np.sum(y)

    energy_values = 0.5 * y_values**2  # Calculate the energies

    return energy_values

a= 4
l = 1
num_terms = 10

# Using power series expansion method
power_series_energies = power_series_expansion_method(a, l, num_terms)
min_energy_power_series = np.min(power_series_energies)
max_energy_power_series = np.max(power_series_energies)

print("Power Series Expansion Method:")
print("Minimum Energy:", min_energy_power_series)
print("Maximum Energy:", max_energy_power_series)

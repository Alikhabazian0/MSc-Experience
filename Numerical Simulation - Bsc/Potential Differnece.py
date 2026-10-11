"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

# Constants
k = 1/4*np.pi
length = 9
charge_density = 2  # 2 coulombs per centimeter
distance = 0.9  # 9 mm = 0.9 cm

# Parameters for Jacobi method
num_iterations = 1000
tolerance = 1e-6

# Calculate the potential
num_points = 100  # Number of points along the rod
delta_x = length / (num_points - 1)
x_values = np.linspace(0, length, num=num_points)
potential = np.zeros(num_points)

# Apply boundary conditions
potential[0] = 0  # Potential at x = 0
potential[-1] = k * charge_density * length  # Potential at x = length

# Perform Jacobi iterations
for iteration in range(num_iterations):
    previous_potential = np.copy(potential)
    for i in range(1, num_points - 1):
        potential[i] = 0.5 * (previous_potential[i - 1] + previous_potential[i + 1])

    # Check convergence
    if np.max(np.abs(potential - previous_potential)) < tolerance:
        break

# Calculate the potential difference at a specific distance
index = int(distance / delta_x)
potential_difference = potential[index] - potential[0]

# Print the results
print("Potential along the rod:")
for x, potential in zip(x_values, potential):
    print(f"x = {x:.2f} cm, Potential = {potential:.2f} volts")

print("\nPotential difference at a distance of 9 mm:")
print(f"Potential difference = {potential_difference:.2f} volts")

"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

# Constants and parameters
side_length = 20  # length of the square border in cm
grid_size = 100  # number of grid points per side
target_potential = 25  # target potential value for approximation
tolerance = 1e-5  # convergence tolerance
max_iterations = 1000  # maximum number of iterations

# Calculate grid spacing
dx = side_length / (grid_size - 1)

# Initialize the potential grid
potential = np.zeros((grid_size, grid_size))

# Set boundary conditions
potential[0, :] = 100  # top boundary
potential[-1, :] = 0  # bottom boundary

# Gauss-Seidel iteration
iteration = 0
converged = False

while iteration < max_iterations and not converged:
    previous_potential = potential.copy()

    # Update potential values in the interior of the grid
    potential[1:-1, 1:-1] = 0.25 * (potential[2:, 1:-1] + potential[:-2, 1:-1] +
                                   potential[1:-1, 2:] + potential[1:-1, :-2])

    # Check for convergence
    if np.max(np.abs(potential - previous_potential)) < tolerance:
        converged = True

    iteration += 1

# Find points with potential ≈ 25 volts
indices = np.argwhere(np.isclose(potential, target_potential, atol=1))
points = [(idx[0] * dx, idx[1] * dx) for idx in indices]

# Print the approximate points with potential ≈ 25 volts
print("Points with potential ≈ 25 volts:")
for point in points:
    print(f"({point[0]} cm, {point[1]} cm)")

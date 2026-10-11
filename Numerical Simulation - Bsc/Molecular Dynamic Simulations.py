"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

# Constants
kB = 1.38e-23  # Boltzmann constant in J/K

# Initial conditions
density = 100  # atoms per cubic millimeter
temperature = 300  # in Kelvin

# Convert density to atoms per cubic meter
density_m3 = density * 1e18

# Calculate the volume of the system
volume = 1 / density_m3  # in cubic meters

# Calculate the initial velocity of the atoms
# We use the formula for the root mean square speed: v = sqrt(3kT/m)
# Assuming the gas is monoatomic with atomic mass m = 40u (like argon)
m = 40 * 1.66e-27  # convert atomic mass unit to kg
v = np.sqrt(3 * kB * temperature / m)

print(f"Initial conditions for the molecular dynamics simulation:")
print(f"Density: {density_m3} atoms/m^3")
print(f"Volume: {volume} m^3")
print(f"Initial velocity: {v} m/s")

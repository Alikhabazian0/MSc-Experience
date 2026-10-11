"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
import matplotlib.pyplot as plt

def calculate_energy(spins):
    energy = 0
    n = len(spins)
    for i in range(n):
        for j in range(n):
            left_neighbor = spins[i, (j-1) % n]
            right_neighbor = spins[i, (j+1) % n]
            top_neighbor = spins[(i-1) % n, j]
            bottom_neighbor = spins[(i+1) % n, j]
            energy += -spins[i, j] * (left_neighbor + right_neighbor + top_neighbor + bottom_neighbor)
    return energy

def minimize_energy(spins):
    energy = calculate_energy(spins)
    while True:
        new_spins = np.copy(spins)
        for i in range(len(spins)):
            for j in range(len(spins)):
                new_spins[i, j] = -spins[i, j]
                new_energy = calculate_energy(new_spins)
                if new_energy < energy:
                    spins = np.copy(new_spins)
                    energy = new_energy
                else:
                    new_spins[i, j] = spins[i, j]  # Revert the spin change if energy doesn't decrease
        if np.array_equal(spins, new_spins):
            break
    return spins, energy

# Set the size of the spin network
n = 10

# Initialize a random spin configuration
spins = np.random.choice([-1, 1], size=(n, n))

# Minimize the energy to find the ground state
new_spins, ground_state_energy = minimize_energy(spins)

# Display the ground state configuration
plt.imshow(new_spins, cmap='binary', interpolation='nearest')
plt.title('Ground State Configuration')
plt.show()

"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
import matplotlib.pyplot as plt

# Set the numbers of random numbers to generate
numbers = [100000, 1000000, 10000000, 100000000, 1000000000]

# Simulation parameters
N = 10000  # Number of particles
T = 1000   # Number of steps

# Perform simulation for each number of random numbers
for num in numbers:

    # Generate random numbers for the walk
    walks = np.random.choice([-1, 1], size=(N, T))

    # Calculate positions and squared positions
    positions = np.cumsum(walks, axis=1)
    pos_sq = positions ** 2

    # Calculate mean squared positions and RMS
    mean_pos_sq = np.mean(pos_sq, axis=0)
    rms = np.sqrt(mean_pos_sq)

    # Plot the RMS
    t = np.arange(T) + 1
    plt.plot(t, rms, label=f'N = {num}')

# Add labels and legend to the plot
plt.xlabel('Time')
plt.ylabel('RMS')
plt.title('RMS of Random Walks')
plt.legend()

# Show the plot
plt.show()

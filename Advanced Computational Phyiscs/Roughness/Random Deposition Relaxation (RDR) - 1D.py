import numpy as np
import matplotlib.pyplot as plt

# Parameters
surface_length = 100  # Length of the 1D surface
total_steps = 1000    # Total time steps

# Initialize the 1D surface (as a list)
surface = [0] * surface_length

# Lists to store roughness and time
roughness_values = []
time_values = []

# Perform random deposition with neighbor selection
for t in range(total_steps):
    # Choose a random position to deposit a particle
    position = np.random.randint(0, surface_length)
    
    # Determine the positions to consider (current, left, and right)
    positions_to_check = [position, position - 1, position + 1]
    
    # Ensure that positions are within the bounds of the surface
    positions_to_check = [p for p in positions_to_check if 0 <= p < surface_length]
    
    # Choose the position with the minimum height
    min_height_position = min(positions_to_check, key=lambda p: surface[p])
    
    # Deposit the particle at the chosen position
    surface[min_height_position] += 1
    
    # Calculate the roughness based on the current surface
    roughness = np.std(surface)
    
    # Store the roughness and time values
    roughness_values.append(roughness)
    time_values.append(t)

# Plot roughness based on time
plt.figure(figsize=(10, 6))
plt.plot(time_values, roughness_values)
plt.xlabel("Time")
plt.ylabel("Roughness")
plt.title("Roughness Evolution Over Time (1D Surface with Neighbor Selection)")
plt.grid(True)
plt.show()

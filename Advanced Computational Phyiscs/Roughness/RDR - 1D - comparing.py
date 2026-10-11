import numpy as np
import matplotlib.pyplot as plt

# Function to perform the simulation for a given grid size
def simulate(grid_size, total_steps):
    # Initialize the grid with zeros
    surface = np.zeros((grid_size,))
    
    # Lists to store roughness and time
    roughness_values = []
    time_values = []

    # Perform random deposition with neighbor selection
    for t in range(total_steps):
        # Choose a random position to deposit a particle
        position = np.random.randint(0, grid_size)

        # Determine the positions to consider (current, left, and right)
        positions_to_check = [position, position - 1, position + 1]

        # Ensure that positions are within the bounds of the surface
        positions_to_check = [p for p in positions_to_check if 0 <= p < grid_size]

        # Choose the position with the minimum height
        min_height_position = min(positions_to_check, key=lambda p: surface[p])

        # Deposit the particle at the chosen position
        surface[min_height_position] += 1

        # Calculate the roughness based on the current surface
        roughness = np.std(surface)

        # Store the roughness and time values
        roughness_values.append(roughness)
        time_values.append(t)

    return time_values, roughness_values

# Grid sizes and total steps
grid_sizes = [16, 32, 64, 128]
total_steps = 1000  # You can adjust this value as needed

# Store roughness values for different grid sizes
roughness_data = []

for size in grid_sizes:
    time, roughness = simulate(size, total_steps)
    roughness_data.append((size, time, roughness))

# Plot roughness for all grid sizes in one plot
plt.figure(figsize=(12, 8))
for size, time, roughness in roughness_data:
    plt.plot(time, roughness, label=f"{size}")

plt.xlabel("Time")
plt.ylabel("Roughness")
plt.title("Roughness Evolution Over Time (1D Surface with Neighbor Selection)")
plt.grid(True)
plt.legend()
plt.show()

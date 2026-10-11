"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

def simulate_self_avoiding_walk(num_steps):
    position = np.array([0, 0])
    positions = [position.copy()]
    visited = set(position.tobytes())

    for _ in range(num_steps):
        step = np.random.choice(4)  # Randomly choose an index: 0, 1, 2, or 3
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]][step]  # Map index to a 2D move
        new_position = position + move

        while new_position.tobytes() in visited:
            step = np.random.choice(4)
            move = [[-1, 0], [1, 0], [0, -1], [0, 1]][step]
            new_position = position + move

        position = new_position
        positions.append(position.copy())
        visited.add(position.tobytes())

    return positions

num_steps = 1000000
num_simulations = 10
beta_view_sum = 0.0

for _ in range(num_simulations):
    positions = simulate_self_avoiding_walk(num_steps)
    beta_view = len(set(tuple(pos) for pos in positions)) / num_steps
    beta_view_sum += beta_view

average_beta_view = beta_view_sum / num_simulations
print("Average Beta View:", average_beta_view)
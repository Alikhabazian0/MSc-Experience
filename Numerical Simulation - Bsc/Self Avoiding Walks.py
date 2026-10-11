"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

def self_avoiding_walk():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    position = (0, 0)
    path = [position]
    visited = {position}

    while True:
        valid_moves = [dir for dir in directions if (position[0] + dir[0], position[1] + dir[1]) not in visited]
        if not valid_moves:
            break
        move = valid_moves[np.random.randint(len(valid_moves))]
        position = (position[0] + move[0], position[1] + move[1])
        path.append(position)
        visited.add(position)

    return path

n_simulations = 20
beta_views = []
time_to_fatigue = []

for _ in range(n_simulations):
    path = self_avoiding_walk()
    beta_view = len(set(path)) / len(path)
    beta_views.append(beta_view)
    time_to_fatigue.append(len(path))

average_beta_view = np.mean(beta_views)
average_time_to_fatigue = np.mean(time_to_fatigue)

print(f"Average Beta View: {average_beta_view}")
print(f"Average Time to Fatigue: {average_time_to_fatigue}")

import random

distances = {
    'A': {'B': 2.24, 'C': 3.16, 'D': 4.24},
    'B': {'A': 2.24, 'C': 2.24, 'D': 2.24},
    'C': {'A': 3.16, 'B': 2.24, 'D': 2},
    'D': {'A': 4.24, 'B': 2.24, 'C': 2}
}

visited = []
path = []

# select the next unvisited city randomly
def select_next_city(current_city):
    unvisited_cities = [city for city in distances[current_city] if city not in visited]
    return random.choice(unvisited_cities)

# Function to check the conditions
def check_conditions(city):
    if visited.count('C') == 1 and visited.count(city) == 1:
        return True
    elif visited.count('C') == 0 and city == 'D':
        return True
    else:
        return False

# Start from an arbitrary city
current_city = random.choice(list(distances.keys()))

# Visit the starting city
visited.append(current_city)
path.append(current_city)

# Loop until all cities are visited
while len(visited) < len(distances):
    # Select the next unvisited city
    next_city = select_next_city(current_city)
    
    # Check the conditions of the purpose
    if check_conditions(next_city):
        visited.append(next_city)
        path.append(next_city)
        current_city = next_city
    else:
        continue

# Visit C-City twice
path.append('C')

# Print the final path
print("Final Path:", ' -> '.join(path))

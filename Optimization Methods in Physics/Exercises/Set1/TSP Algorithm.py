import random

distances = {
    'ab': 2.24,
    'bd': 2.24,
    'bc': 2.24,
    'cd': 2,
    'ac': 3.16,
    'ad': 4.24
}

def nearest_unvisited_city(city, visited):
    nearest_city = None
    nearest_distance = float('inf')
    for key, value in distances.items():
        if city in key:
            other_city = key.replace(city, '')
            if other_city not in visited and value < nearest_distance:
                nearest_city = other_city
                nearest_distance = value
    return nearest_city

def next_unvisited_city_random(city, visited):
    unvisited_cities = [key.replace(city, '') for key in distances.keys() if city in key and key.replace(city, '') not in visited]
    return random.choice(unvisited_cities) if unvisited_cities else None

#Greedy_algorithm
def tsp_greedy(start_city):
    visited = set()
    path = [start_city]
    visited.add(start_city)
    
    while len(visited) < len(distances):
        next_city = next_unvisited_city_random(path[-1], visited)
        if next_city:
            path.append(next_city)
            visited.add(next_city)
        else:
            break

    path.append(start_city)

    return path

start_city = 'b'
final_path = tsp_greedy(start_city)
print("Final Path:", final_path)


import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/09/input_a.txt', 'r')]

# dictionary for distances
distances = defaultdict(dict)

# parse input
for line in lines:
    parts = line.split()
    from_city = parts[0]
    to_city = parts[2]
    distance = int(parts[4])

    # add to dictionary
    if from_city not in distances:
        distances[from_city] = defaultdict(int)
    if to_city not in distances:
        distances[to_city] = defaultdict(int)

    distances[from_city][to_city] = distance
    distances[to_city][from_city] = distance

# find shortest path that visits all cities
def find_shortest_path(distances, visited, current_city):
    # if all cities are visited, return 0
    if len(visited) == len(distances):
        return 0

    # set distance to infinity
    min_distance = float('inf')

    # loop through all cities
    for city in distances:
        # if city is not visited
        if city not in visited:
            # add city to visited
            visited.add(city)
            # find distance to next city
            distance = find_shortest_path(distances, visited, city)
            # remove city from visited
            visited.remove(city)
            # add distance to total distance
            min_distance = min(min_distance, distances[current_city][city] + distance)

    return min_distance

# find shortest path
all_dist = []
for city in distances:
    all_dist.append(find_shortest_path(distances, set(), city))
print(min(all_dist))
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

# find longest path that visits all cities
def find_longest_path(city, distances, visited, all_distances):
    if len(visited) == len(distances):
        print(visited)
        total_dist = sum([distances[visited[i]][visited[i+1]] for i in range(len(visited)-1)])
        print(total_dist)
        all_distances.append(total_dist)
    
    for subcity in [x for x in distances[city] if x not in visited]:
        visited.append(subcity)
        find_longest_path(subcity, distances, visited, all_distances)
        visited.pop()
    
all_distances = []
for city in distances:
    find_longest_path(city, distances, visited = [city], all_distances = all_distances)

print(max(all_distances))
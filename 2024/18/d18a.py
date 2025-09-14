import os
import math
import re

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# point class
class Point:
    def __init__(self, x, y):
        self.id = str(x) + '_' + str(y)
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

# define a quick distance function
distance = lambda P1, P2: math.sqrt(pow((P1.x - P2.x), 2) + pow((P1.y - P2.y), 2))

# graph structure
G = {}

# define start and end positions 
# start is always 0,0, but end is 6,6 for sample and 70, 70 for real data
grid_max_x = 70
grid_max_y = 70
S = Point(0, 0)
E = Point(grid_max_x, grid_max_y)

# tracker for all points
points = []
for x in range(grid_max_x + 1):
    for y in range(grid_max_y + 1):
        p = Point(x,y)
        points.append(p)

# import corrupted memory
corrupted_points = []
for line in open('2024/18/input_a.txt', 'r').readlines():
    num_matches = re.findall(r'\d+', line)
    p = Point(int(num_matches[0]), int(num_matches[1]))
    corrupted_points.append(p)

# set how many bytes (points) to use as cutoff
cutoff_bytes = 1024
for i in range(cutoff_bytes):
    cp = corrupted_points.pop(0)
    points.remove(cp)

# create graph of all valid points
for p in points:
    G[p] = {}

    # find all neighbours
    ns = [n for n in points if distance(p, n) == 1]
    for n in ns:
        if n not in G[p]:
            G[p][n] = 1

def dijkstra(G, S, E):
    dist = {}
    prev = {}
    Q = []

    for v in G:
        dist[v] = 999999999
        prev[v] = None
        Q.append(v)
    
    dist[S] = 0
    prev[S] = None

    while len(Q) > 0:
        max_dist = 999999999
        u = None
        for u_ in Q:
            if dist[u_] < max_dist:
                max_dist = dist[u_]
                u = u_

        if u is not None:        
            Q.remove(u)
        else:
            return dist, prev

        for v in G[u]:
            if v in Q:
                alt = dist[u] + G[u][v]

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        
        if u == E:
            return dist, prev
    
    return dist, prev
        
dist, prev = dijkstra(G, S, E)
print(dist[E])
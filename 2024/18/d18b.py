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

# the man, the myth, the legend: dijkstra
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

# determine when the exit will be blocked
# do a binary search between 1024 and the total number of corrupted bytes (3450)
start_ = 1024
end_ = len(corrupted_points)
def binary_search(S, E, points, corrupted_points, start, end):
    middle = start + int((end - start) / 2)

    if middle == start or middle == end:
        print("Occurs at n-th corrupted byte", start)
        return middle

    points_ = points.copy()
    corrupted_points_ = corrupted_points.copy()

    # set how many bytes (points) to use as cutoff
    cutoff_bytes = middle
    for i in range(cutoff_bytes):
        cp = corrupted_points_.pop(0)
        points_.remove(cp)

    # create graph of all valid points
    for p in points_:
        G[p] = {}

        # find all neighbours
        ns = [n for n in points_ if distance(p, n) == 1]
        for n in ns:
            if n not in G[p]:
                G[p][n] = 1
    
    dist, prev = dijkstra(G, S, E)
    if dist[E] == 999999999:
        print("Deadly corrupted byte occurs between", start, 'and', middle)
        return binary_search(S, E, points, corrupted_points, start, middle)
    else:
        print("Deadly corrupted byte occurs between", middle, 'and', end)
        return binary_search(S, E, points, corrupted_points, middle, end)

# find the terminal point and get the coordinates
terminal_point = binary_search(S, E, points, corrupted_points, start_, end_)
print(corrupted_points[terminal_point])
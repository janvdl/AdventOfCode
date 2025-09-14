from enum import Enum
import os
import math

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define directions
class direction(Enum): 
    north = [-1, 0 ]
    south = [ 1, 0 ]
    west  = [ 0, -1]
    east  = [ 0, 1 ]

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

# define start and end positions
S = Point(0, 0)
E = Point(0, 0)

# graph structure
G = {}

# import map data and find Start and End positions
map = [line.strip() for line in open('2024/16/input_sample.txt', 'r').readlines()]
points = []

for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == '.':
            P = Point(x, y)
            points.append(P)
            G[P] = {}
        elif map[x][y] == 'S':
            S = Point(x, y)
            G[S] = {}
        elif map[x][y] == 'E':
            E = Point(x, y)
            G[E] = {}
            points.append(E)
        else:
            pass # this is a wall or empty space

visited = []
Q = [S]
while len(Q) > 0:
    p = Q.pop()
    visited.append(p)
    if p not in G:
        G[p] = {}

    neighbours = [n for n in points if distance(p, n) == 1]
    for neighbour in neighbours:
        if neighbour not in G[p]:
            G[p][neighbour] = 1
            #print("Edge between", p, "and", neighbour)
            Q.append(neighbour)

# Use Dijkstra to find the shortest path / minimum weights
def dijkstra(G, S, E):
    dist = {}
    prev = {}
    Q = []
    node_direction = {}

    for v in G:
        dist[v] = 999999999
        prev[v] = None
        Q.append(v)
    
    dist[S] = 0
    prev[S] = Point(S.x + direction.west.value[0], S.x + direction.west.value[1])
    node_direction[S] = direction.east.value

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
                if (v.x != prev[u].x and v.y != prev[u].y):
                    alt += 1000

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    #print("U = ", u, ", V = ", v, "dist =", dist[v])
        
        if u == E:
            return dist, prev
    
    return dist, prev
        

dist, prev = dijkstra(G, S, E)
print(dist[E])

seq = []
u = E
while(u != S):
    seq.insert(0, u)
    u = prev[u]

print(len(seq))
import os
import math

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# distance function
def dist(p, q) -> float:
    p0, p1, p2 = p[0], p[1], p[2]
    q0, q1, q2 = q[0], q[1], q[2]

    distance = math.sqrt((p0 - q0)**2 + (p1 - q1)**2 + (p2 - q2)**2)
    return distance

# connected components function
def comp_all_connected(G) -> bool:
    visited = set()
    circuits = []

    for node in G:
        if node not in visited:
            stack = [node]
            circuit = []

            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    circuit.append(v)
                    for u in G[v]:
                        stack.append(u)

            circuits.append(tuple([len(circuit), circuit]))

            if len(circuits) > 1:
                return False
    
    return True

# read input and make a list of points
points = []
for l in open('2025/08/input.txt', 'r').readlines():
    coords = tuple([int(x) for x in l.strip().split(",")])
    points.append(coords)

# loop over points to find min_distance
dists = []
for p_idx in range(len(points)):
    for q_idx in range(p_idx + 1, len(points)):
        tmp_dist = dist(points[p_idx], points[q_idx])
        dists.append(tuple([tmp_dist, points[p_idx], points[q_idx]]))
dists.sort()

# get the shortest distances and their assoc. points
# place these into an adjacency list graph
G = {}
prev_count = 0
for d in dists:
    _, p, q = d[0], d[1], d[2]
    if p not in G:
        G[p] = []
    if q not in G:
        G[q] = []

    G[p].append(q)
    G[q].append(p)

    if comp_all_connected(G) and len(G) == len(points):
        print(p)
        print(q)
        print(f"Product of {p[0]} and {q[0]} is {p[0] * q[0]}")
        break
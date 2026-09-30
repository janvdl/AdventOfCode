import os
from collections import defaultdict

debug = False
if debug:
    n = 10
    x_dims = 10
    y_dims = 7
    start = (1, 1)
    goal = (7, 4)
else:
    n = 1362
    x_dims = 35
    y_dims = 45
    start = (1, 1)
    goal = (31, 39)

# wall vs open space function
def is_wall(x, y, n):
    f = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    d = f + n
    b = bin(d)[2:]

    num_of_ones = sum(1 for c in b if int(c) % 2 == 1)
    
    return num_of_ones % 2 != 0

# pathfinding function
def best_path(adj, start: tuple, goal: tuple, path: set):
    best = 999
    if start == goal:
        return 0
    else:
        for child in adj[start]:
            if child not in path:
                path.add(child)
                best = min(best, 1 + best_path(adj, child, goal, path))
                path.remove(child)

    return best

# init dict for grid
points = []
adj = defaultdict(set)

# calculate all open points and build an adjacency graph
for x in range(x_dims):
    for y in range(y_dims):
        if not is_wall(x, y, n):
            points.append((x, y))

# this is O(n^2), but the input is small enough
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]

        diff = (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
        if (diff[0] == 1 and diff[1] == 0) or (diff[0] == 0 and diff[1] == 1):
            # single block distance away (no diags) and is adjacent
            adj[p1].add(p2)
            adj[p2].add(p1)

# calculate least cost path by DFSing adjacency list
best = best_path(adj, start, goal, path={start})
print(best)
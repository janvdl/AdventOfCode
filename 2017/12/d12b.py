import os
from collections import defaultdict

debug = False
if debug:
    lines = [l.strip() for l in open('2017/12/input_sample.txt', 'r').readlines()]
else:
    lines = [l.strip() for l in open('2017/12/input.txt', 'r').readlines()]

adj = defaultdict(list)

# build the adjacency list
tovisit = []
visited = []
components = 0

for line in lines:
    from_, to_ = line.split('<->')[0].strip(), line.split('<->')[1].replace(" ", "").split(',')

    tovisit.append(from_)

    if from_ not in adj:
        for t in to_:
            adj[from_].append(t)

# search from 0 through the adjacency list
while len(tovisit) > 0:
    components += 1

    v = tovisit.pop(0)
    visited.append(v)
    neighbours = list(adj[v])

    while len(neighbours) > 0:
        u = neighbours.pop()
        if u in visited:
            continue
        else:
            visited.append(u)
            tovisit.remove(u)
            neighbours += adj[u]

print("No. of components:", components)
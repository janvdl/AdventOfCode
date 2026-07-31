import os
from collections import defaultdict
from treelib import Tree, Node

debug = False
if debug:
    lines = [l.strip() for l in open('2017/12/input_sample.txt', 'r').readlines()]
else:
    lines = [l.strip() for l in open('2017/12/input.txt', 'r').readlines()]

adj = defaultdict(list)

# build the adjacency list
for line in lines:
    from_, to_ = line.split('<->')[0].strip(), line.split('<->')[1].replace(" ", "").split(',')

    if from_ not in adj:
        for t in to_:
            adj[from_].append(t)

# search from 0 through the adjacency list
known = ['0']
unknown = list(adj['0'])

while(len(unknown) > 0):
    u = unknown.pop()
    if u in known:
        continue
    else:
        known.append(u)
        unknown += adj[u]

print(known)
print(len(known))
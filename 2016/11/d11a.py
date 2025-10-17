import os
from helpers import *
from copy import deepcopy
import json

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# === data structures

# building
b = {}
b[0] = ['POLG', 'THUG', 'THUM', 'PROG', 'RUTG', 'RUTM', 'COBG', 'COBM']
b[1] = ['POLM', 'PROM']
b[2] = []
b[3] = []
b['e'] = 0
b = sort_building(b)
jb = json.dumps(b) # create a json dump of the building, this is our start node in g
initial = jb
goal = ''

# adjacency graph
g = {}

# === end data structures

# create a queue containing building and start floor
q = []
q.append(b)

while len(q) > 0:
    print(len(q), '\r', end='')
    b = q.pop(0)

    # get the json dump as node key and add to g
    j = json.dumps(b)
    if j not in g:
        g[j] = []

        if len(b[0]) == 0 and len(b[1]) == 0 and len(b[2]) == 0:
            print('Solution found')
            print(j)
            goal = j
        else:
            # continue trying new combinations to find the solution
            f = b['e']
            cc = new_nodes(b[f])

            fns = []
            if f != 0: fns.append(f - 1)
            if f != 3: fns.append(f + 1)

            for fn in fns:
                for c in cc:
                    # make a copy and save the new elevator location
                    t = deepcopy(b)
                    t['e'] = fn

                    t[f] = list(set(t[f]) - set(c))
                    t[fn] = list(set(t[fn]) | set(c))
                    if is_building_valid(t):
                        t = sort_building(t)
                        tj = json.dumps(t)
                        if tj not in g[j] and tj not in g and t not in q:
                            g[j].append(tj)
                            q.append(t)
                    else:
                        pass # do not continue with this combination

path, dist = shortest_path(g, initial, goal)

for n in path:
    print(n)
print(dist)
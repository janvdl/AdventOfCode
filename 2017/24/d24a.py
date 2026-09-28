import os
from collections import defaultdict

# read input
debug = False
lines = None
if debug:
    lines = open('2017/24/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/24/input.txt', 'r').readlines()

# adjacency list
adj = defaultdict(set)

# treat each input line as an edge and separate the unique nodes
for line in lines:
    edge = line.strip()

    nodes = [int(n) for n in edge.split("/")]
    adj[nodes[0]].add(nodes[1])
    adj[nodes[1]].add(nodes[0])


# dfs accepts the adjacency list graph (G), a start node (n), and a path set (p = [])
def dfs(G, n, p):
    s_max = 0

    for child in G[n]:
        edge = (min(n, child), max(n, child))
        if edge in p:
            continue

        p.add(edge)
        s_max = max(s_max, n + child + dfs(G, child, p))
        p.remove(edge)

    return s_max
    

s_max = dfs(G = adj, n = 0, p = set())
print(f"Maximum strength is {s_max}")
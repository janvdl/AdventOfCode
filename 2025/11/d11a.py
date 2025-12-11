import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# graph for nodes
G = {}
G["out"] = []

# read input
for l in open('2025/11/input.txt', 'r').readlines():
    nodes = l.strip().replace(":", "").split()
    origin = nodes[0]

    # build directional graph
    if origin not in G:
        G[origin] = []
    for dest in nodes[1:]:
        G[origin].append(dest)

# dfs to find all paths
def dfs(start, goal):
    if start == goal:
        return 1
    return sum(dfs(next, goal) for next in G[start])

start = "you"
goal = "out"

print(dfs(start, goal))
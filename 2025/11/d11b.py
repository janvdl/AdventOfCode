import os
from functools import cache

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
@cache
def dfs(start, goal):
    if start == goal:
        return 1
    return sum(dfs(next, goal) for next in G[start])

svr_fft_dac_out = dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
svr_dac_fft_out = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")

print(svr_dac_fft_out + svr_fft_dac_out)
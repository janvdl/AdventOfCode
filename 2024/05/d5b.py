from math import ceil
import re

# graph
G = {}

# paths to check
paths = []

# valid paths
valid_paths = []
invalid_paths = []

# known valid/invalid edges - to avoid rechecking known good/bad ones
valid_edges = []
invalid_edges = []

# dfs to check if path is valid
def path_is_valid(start, goal):
    if start in G:
        nodes = G[start]
        if goal in nodes:
            return True
        elif len(nodes) > 0:
            for node in nodes:
                path_is_valid(node, goal)
    
    return False

# read input data and parse
with open('input_b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "|" in line:
            rule_matches = re.findall(r'(\d+)\|(\d+)', line)
            for rule in rule_matches:
                start_node = int(rule[0])
                end_node = int(rule[1])

                if start_node in G:
                    G[start_node].append(end_node)
                else:
                    G[start_node] = []
                    G[start_node].append(end_node)
        elif "," in line:
            temp_path = line.replace("\n", "").split(",")
            temp_path = list(map(int, temp_path))
            paths.append(temp_path)

# evaluate each path for validity
path_count = len(paths)
path_index = 0
for path in paths:
    path_index += 1
    print("Evaluating path", path_index, "of", path_count, ": ", path)
    is_valid = True
    edge_pairs = zip(path, path[1:])
    for edge in edge_pairs:
        if edge in valid_edges:
            continue
        elif edge in invalid_edges:
            is_valid = False
            break
        elif not path_is_valid(edge[0], edge[1]):
            invalid_edges.append(edge)
            is_valid = False
            break
        else:
            valid_edges.append(edge)
    
    if is_valid:
        #valid_paths.append(path)
        continue
    else:
        invalid_paths.append(path)

# define Kahn's function for topological sorting
def findNodesWithoutIncomingEdges(G):
    nodesNoIncoming = [x for x in G]

    for node in G:
        nodes_with_incoming = G[node]
        nodesNoIncoming = list(set(nodesNoIncoming) - set(nodes_with_incoming))

    return nodesNoIncoming

def kahn(G, path):
    H = {x: G.get(x, []) for x in path} # obtain a smaller subgraph of the nodes of interest in the path only
    #print(H)

    L = []
    S = findNodesWithoutIncomingEdges(H)

    while len(S) > 0:
        n = S.pop()
        L.append(n)
        #print("S: ", L)
        #print("L: ", L)

        H.pop(n)
        S = list(set(findNodesWithoutIncomingEdges(H)) - set(L))
        
    #print("Original path: ", path)
    #print("Kahn sorted path: ", L)

    return L


# run all invalid paths through Kahn's topological sort algorithm
# and add up the total of the middle numbers
total = 0
for invalid_path in invalid_paths:
    L = kahn(G, invalid_path)
    middle = ceil(len(L) / 2) - 1
    total += L[middle]
print("Total of middle elements of invalid paths fixed by Kahn's algorithm: ", total)
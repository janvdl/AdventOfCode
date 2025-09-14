from math import ceil
import re

# graph
G = {}

# paths to check
paths = []

# valid paths
valid_paths = []

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
with open('input_sample.txt', 'r') as file:
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
        valid_paths.append(path)

# get middle number for all valid paths and add them up
total = 0
for valid_path in valid_paths:
    middle = ceil(len(valid_path) / 2) - 1
    total += valid_path[middle]
print("Total of middle elements of valid paths: ", total)
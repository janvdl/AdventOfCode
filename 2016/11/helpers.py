from itertools import combinations
from collections import deque

# function to check if building is valid
def is_building_valid(b):
    for k,v in b.items():
        if k != 'e':
            if not is_floor_valid(b[k]):
                return False
    return True

# function to check if proposed contents in any given floor are valid
known_invalid = []
def is_floor_valid(contents):
    contents = sorted(contents)
    if contents in known_invalid:
        return False
    
    generators = []
    microchips = []
    for c in contents:
        if c[-1] == 'M':
            microchips.append(c[:-1])
        elif c[-1] == 'G':
            generators.append(c[:-1])

    # make sure if there are generators that the microchips are protected
    # by a matching generator
    for x in microchips[:]:
        if x in generators:
            generators.remove(x)
            microchips.remove(x)

    if len(generators) > 0 and len(microchips) > 0:
        known_invalid.append(contents)
        return False


    # no failures, contents valid
    return True

# function to generate new, valid nodes
def new_nodes(floor_contents):
    # get all 1 combinations from this floor
    comb1 = list(combinations(floor_contents, 1))

    # get all 2 combinations from this floor
    comb2 = list(combinations(floor_contents, 2))

    # evaluate all combinations for validity
    # and store valid combinations
    valid = []
    for c in (comb2 + comb1):
        if is_floor_valid(c):
            valid.append(list(c))

    return valid

def sort_building(building):
    for k,v in building.items():
        if k != 'e':
            building[k] = sorted(v)
    
    return building

def shortest_path(graph, start, goal):
    if start == goal:
        return [start], 0  # Path is just the node itself
    
    visited = set()
    queue = deque([(start, [start])])  # (current_node, path_so_far)
    
    while queue:
        node, path = queue.popleft()
        
        if node in visited:
            continue
        visited.add(node)
        
        # Normalize neighbors (some entries might be strings instead of lists)
        neighbors = graph.get(node, [])
        if isinstance(neighbors, str):
            neighbors = [neighbors]
        
        for neighbor in neighbors:
            if neighbor == goal:
                return path + [neighbor], len(path)  # distance = edges = path length - 1
            queue.append((neighbor, path + [neighbor]))
    
    return None, None  # No path found
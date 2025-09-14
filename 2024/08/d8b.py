import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# dictionaries for node and antinode locations
nodes = {}
antinodes = {}

# grid constraints
grid_max_x = 0
grid_max_y = 0

# import node data and set grid constraints
i = -1
lines = [line.strip() for line in open('input_b.txt', 'r').readlines()]
grid_max_x = len(lines) - 1
grid_max_y = len(lines[0]) - 1

for line in lines:
    i += 1 # x-index of node
    for j in range(len(line)): # y-index of node
        curr_char = line[j]
        if curr_char != '.':
            if curr_char not in nodes:
                nodes[curr_char] = []
                antinodes[curr_char] = [] # while we're here, initialise the antinodes dict as well
            nodes[curr_char].append([i, j])

# function to check if a coord is within grid range
def isCoordValid(coord):
    global grid_max_x
    global grid_max_y

    return coord[0] >= 0 and coord[0] <= grid_max_x and coord[1] >= 0 and coord[1] <= grid_max_y

# for each node key, create pairs of node coords and generate antinodes
for node in nodes:
    if len(nodes[node]) > 1: # no point looking for antinodes if there's only one node
        for i in range(len(nodes[node])):
            for j in range(i + 1, len(nodes[node])):
                node1 = nodes[node][i]
                node2 = nodes[node][j]

                node1_left = (node1[1] < node2[1]) # check if first node is to the left of the second
                x_dist = abs(node1[0] - node2[0])
                y_dist = abs(node1[1] - node2[1])

                # figure out how many additional antinodes can roughly fit on this map
                # some of these will be outside of the map grid, discard those later when counting unique locations
                maxloops = int(min(grid_max_x / x_dist, grid_max_y / y_dist)) + 1

                for k in range(maxloops):
                    antinode1 = [node1[0] - (x_dist * k), node1[1] - (y_dist * k) if node1_left else node1[1] + (y_dist * k)]
                    antinode2 = [node2[0] + (x_dist * k), node2[1] + (y_dist * k) if node1_left else node2[1] - (y_dist * k)]

                    antinodes[node].append(antinode1)
                    antinodes[node].append(antinode2)

# check all antinodes and count only the ones within the map constraints
unique_locations = []
for antinode in antinodes:
    for coord in antinodes[antinode]:
        if coord not in unique_locations and isCoordValid(coord):
            unique_locations.append(coord)
print(len(unique_locations))
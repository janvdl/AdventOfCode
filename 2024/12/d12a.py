import os
import math
from collections import defaultdict

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# dict for regions
regions = defaultdict(list)

# grid constraints
grid_max_x = 0
grid_max_y = 0

# import data
map  = [list(line.strip()) for line in open('input_a.txt', 'r').readlines()]
grid_max_x = len(map) - 1
grid_max_y = len(map[0]) - 1
#print(map)

# flood fill algorithm to find regions
colour_map = [[0 for _ in range(grid_max_x + 1)] for _ in range(grid_max_y + 1)]
# colour counter
colour = 1

def flood(q, c):
    global colour, colour_map

    while len(q) > 0:
        p = q.pop(0)
        x = p[0]
        y = p[1]

        if colour_map[x][y] == 0:
            cell = map[x][y]

            # if the current cell is the same as the initial cell
            # then we are 'inside' the same region
            if cell == c:
                colour_map[x][y] = colour
                regions[colour].append([x, y])

                if x > 0:
                    q.append([x - 1, y])
                if x < grid_max_x:
                    q.append([x + 1, y])
                if y > 0:
                    q.append([x, y - 1])
                if y < grid_max_y:
                    q.append([x, y + 1])
    
    #print(colour_map)
    colour += 1 # increment the colour for the next region

# go through every block on the colour map and assign a colour to all contiguous regions
# the flood() function updates the colour map while the for loop is running
for x in range(len(colour_map)):
    for y in range(len(colour_map)):
        if colour_map[x][y] == 0:
            q = []
            q.append([x, y])
            flood(q, map[x][y])

# define a quick distance function
distance = lambda x1, y1, x2, y2: math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

# with the regions dictionary defined, we have the area size, now find the outer perimeter
# find the number of neighbours for each cell
# 0 neighbours = 4 fences
# 1 neighbour = 3 fences
# 2 neighbours = 2 fences
# 3 neighbours = 1 fence
# 4 neighbours = 0 fences
total_fencing_price = 0
for r in regions:
    fences_for_region = 0
    areas_in_region = len(regions[r])
    for point in regions[r]:
        neighbours = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) == 1]
        fences_needed = 4 - len(neighbours)
        fences_for_region += fences_needed

        #print("Region", r, "has elements", regions[r], "with area", areas_in_region, "and fences needed", fences_for_region)

    total_fencing_price += (fences_for_region * areas_in_region)
print(total_fencing_price)
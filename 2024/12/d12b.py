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

# this code is garbage but it works and is organic, non-AI, crafted-with-love-by-human-hands code
total_fencing_price = 0
for r in regions:
    areas_in_region = len(regions[r])
    corners_for_region = 0
    
    if areas_in_region == 1:
        corners_for_region = 4 # always 4 corners for a single block
    elif areas_in_region == 2:
        corners_for_region = 4 # 2 blocks can only be arrabged to have 4 corners
    else:
        for point in regions[r]:
            # check around each cell to determine how many corners it should have
            neighbours_above = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) == 1 and point[0] > x[0]]
            neighbours_below = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) == 1 and point[0] < x[0]]
            neighbours_left  = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) == 1 and point[1] > x[1]]
            neighbours_right = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) == 1 and point[1] < x[1]]
            neighbours_above_left = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) < 1.5 and point[0] > x[0] and point[1] > x[1]]
            neighbours_above_right = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) < 1.5 and point[0] > x[0] and point[1] < x[1]]
            neighbours_below_left = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) < 1.5 and point[0] < x[0] and point[1] > x[1]]
            neighbours_below_right = [x for x in regions[r] if distance(point[0], point[1], x[0], x[1]) < 1.5 and point[0] < x[0] and point[1] < x[1]]

            has_neighbour_above = len(neighbours_above) == 1
            has_neighbour_below = len(neighbours_below) == 1
            has_neighbour_left  = len(neighbours_left)  == 1
            has_neighbour_right = len(neighbours_right) == 1
            has_neighbour_above_left = len(neighbours_above_left) == 1
            has_neighbour_above_right = len(neighbours_above_right) == 1
            has_neighbour_below_left = len(neighbours_below_left) == 1
            has_neighbour_below_right = len(neighbours_below_right) == 1

            #print("Point", point, "has L:", has_neighbour_left, ", R:", has_neighbour_right, ", T:", has_neighbour_above, ", B:", has_neighbour_below, ", TL:", has_neighbour_above_left, ", TR:", has_neighbour_above_right, ", BL:", has_neighbour_below_left, ", BR:", has_neighbour_below_right)

            count_top_left  = 1 if not has_neighbour_left and not has_neighbour_above else 0
            count_top_right = 1 if not has_neighbour_right and not has_neighbour_above else 0
            count_bot_left  = 1 if not has_neighbour_left and not has_neighbour_below else 0
            count_bot_right = 1 if not has_neighbour_right and not has_neighbour_below else 0

            count_top_left_diag  = 1 if has_neighbour_left and has_neighbour_above and not has_neighbour_above_left else 0
            count_top_right_diag = 1 if has_neighbour_right and has_neighbour_above and not has_neighbour_above_right else 0
            count_bot_left_diag  = 1 if has_neighbour_left and has_neighbour_below and not has_neighbour_below_left else 0
            count_bot_right_diag = 1 if has_neighbour_right and has_neighbour_below and not has_neighbour_below_right else 0

            corners_for_point = count_top_left + count_top_right + count_bot_left + count_bot_right + count_top_left_diag + count_top_right_diag + count_bot_left_diag + count_bot_right_diag
            corners_for_region += corners_for_point
            #print("Point", point, "has", corners_for_point, "corners")

    print("Region", r, "has elements", regions[r], "with area", areas_in_region, "and corners", corners_for_region)
    #input()

    total_fencing_price += (corners_for_region * areas_in_region)
print(total_fencing_price)
import os
from collections import defaultdict
from knot_hash import knot_hash_bin

debug = False
if debug:
    key = open('2017/14/input_sample.txt', 'r').readline()
else:
    key = open('2017/14/input.txt', 'r').readline()

# grid building starts here
grid = defaultdict(str)
for i in range(0, 128):
    curr_key = key + "-" + str(i)
    b = knot_hash_bin(curr_key) # returns binary string 10100000110000100000000101110000...
    for j, v in enumerate(b):
        grid[(i,j)] = '#' if v == '1' else '.'

def fill_colour(grid, coord, colour):
    if coord in grid: # dont change dictionary by adding new keys
        if grid[coord] == '#':
            grid[coord] = colour

            up = (coord[0] - 1, coord[1])
            fill_colour(grid, up, colour)

            down = (coord[0] + 1, coord[1])
            fill_colour(grid, down, colour)

            left = (coord[0], coord[1] - 1)
            fill_colour(grid, left, colour)

            right = (coord[0], coord[1] + 1)
            fill_colour(grid, right, colour)
        else:
            pass

def flood_fill(grid):
    colour = 0
    for k in grid.keys():
        if grid[k] == '#':
            colour += 1
            fill_colour(grid, k, str(colour))
    print(f"Colours/regions = {colour}")

flood_fill(grid)
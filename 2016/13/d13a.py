### INCOMPLETE, but 2025 event is starting soon so this one is on ice

import os
import math

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# math function
def is_wall(x, y):
    f = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    n = 1362
    n = 10
    d = f + n
    b = bin(d)[2:]

    num_of_ones = sum(1 for c in b if int(c) % 2 == 1)
    
    return num_of_ones % 2 != 0

# draw map
dims = 40
map = [[0 for x in range(dims)] for y in range(dims)]

for x in range(dims):
    for y in range(dims):
        map[y][x] = '#' if is_wall(x, y) else '.'

for line in map:
    print(line)
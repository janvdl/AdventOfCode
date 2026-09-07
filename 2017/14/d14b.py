import os
from collections import defaultdict
from knot_hash import knot_hash_bin

debug = True
if debug:
    key = open('2017/14/input_sample.txt', 'r').readline()
else:
    key = open('2017/14/input.txt', 'r').readline()

# grid building starts here
grid = [[] for j in range(0, 128)]
for i in range(0, 128):
    curr_key = key + "-" + str(i)
    b = knot_hash_bin(curr_key) # returns binary string 10100000110000100000000101110000...
    grid[i] = ['#' if c == '1' else '.' for c in b]

for row in grid:
    print(row)
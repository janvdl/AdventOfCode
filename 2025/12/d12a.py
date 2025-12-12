import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
info_lines = open('2025/12/input.txt', 'r').read().strip().split("\n\n")

# split into present block information and tree regions/areas
block_shapes = info_lines[:-1]
tree_regions = info_lines[-1].split("\n")

# dictionary to keep track of present sizes
present_sizes = defaultdict(int)

# get the amount of #'s that each block needs
for block in range(len(block_shapes)):
    line = block_shapes[block]
    present_sizes[block] += sum([1 if c == "#" else 0 for c in line])

fit_count = 0
for region in tree_regions:
    dimensions, presents = region.split(":")
    w, h = map(int, dimensions.split("x"))

    tree_area = w * h # this tree area should fit the number of hashes occupied by the presents below
    presents = list(map(int, presents.strip().split()))

    area_req = 0
    for p in range(len(presents)):
        area_req += presents[p] * present_sizes[p]

    if area_req <= tree_area:
        fit_count += 1

print(fit_count)
import os
from collections import defaultdict

# initialise grid
grid = defaultdict(str)
currpos = (0, 0)

# define moves and function to change direction
# move array is [U, R, D, L]
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn(isLeft: bool, currmove: int) -> int:
    if isLeft:
        currmove -= 1
    else:
        currmove += 1

    return currmove % 4

# function to count infections
def countCurrentInfections(grid):
    count = 0
    for k, v in grid.items():
        if v == '#':
            count += 1

    return count

# read input - input is always a square (3x3 for sample, 25x25 for real)
debug = False
lines = None
if debug:
    lines = open('2017/22/input_sample.txt', 'r').readlines()
    currpos = (1, 1)
else:
    lines = open('2017/22/input.txt', 'r').readlines()
    currpos = (12, 12)

for i, line in enumerate(lines):
    for j, v in enumerate(line.strip()):
        grid[(i, j)] = v

# simulate the virus movement
currmove = 0
allInfections = 0
for i in range(10000):
    if grid[currpos] == '#':
        # infected: clean then turn right
        currmove = turn(isLeft=False, currmove=currmove)
        grid[currpos] = '' # if infected, become clean
    else:
        # clean: infect, then turn left
        currmove = turn(isLeft=True, currmove=currmove)
        grid[currpos] = '#'
        allInfections += 1

    # now move in the direction we're facing
    currpos = (currpos[0] + moves[currmove][0], currpos[1] + moves[currmove][1])

print(grid)
print(f'There are currently {countCurrentInfections(grid)} active infections, but a total of {allInfections} were caused during the bursts.')
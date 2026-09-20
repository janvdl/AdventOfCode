import os
from collections import defaultdict

# grid dict
grid = defaultdict(str)

# valid moves
moves = defaultdict(tuple)
moves['up'] = (-1, 0)
moves['down'] = (1, 0)
moves['left'] = (0, -1)
moves['right'] = (0, 1)

# read input
debug = False
lines = None
if debug:
    lines = open('2017/19/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/19/input.txt', 'r').readlines()

# funcs 
def move(coord, direction, jump = 1):
    return (coord[0] + (direction[0] * jump), coord[1] + (direction[1] * jump))

def peek(grid, coord, direction, jump = 1):
    new_coord = move(coord, direction, jump)
    return grid[new_coord]

# init vars
pos = (0, 0) # grid coords = (row, col)
dir = moves['down'] # initial direction is down
empty = ('', ' ')

# populate grid
for i, v in enumerate(lines):
    for j, w in enumerate(lines[i]):
        if i == 0 and w in ['|']:
            pos = (i, j) # find start pos

        grid[(i, j)] = w if w != '\n' else ' '

# run through grid
stringbuilder = ""
steps = 0

halt = False
while not halt:
    steps += 1
    curr_char = grid[pos]
    if curr_char not in ('|', '-', '+', '', ' '):
        stringbuilder += curr_char

    next1 = peek(grid, pos, dir, 1)

    if next1 not in empty:
        pos = move(pos, dir)
    else:
        if dir in (moves['up'], moves['down']):
            left = peek(grid, pos, moves['left'])
            right = peek(grid, pos, moves['right'])
            if left in empty and right in empty:
                halt = True

            dir = moves['left'] if left not in empty else moves['right']
        elif dir in (moves['left'], moves['right']):
            up = peek(grid, pos, moves['up'])
            down = peek(grid, pos, moves['down'])
            if up in empty and down in empty:
                halt = True

            dir = moves['up'] if up not in empty else moves['down']
        pos = move(pos, dir)

print(steps)
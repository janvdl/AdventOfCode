import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# dictionary for storing unique locations
locations = defaultdict(int)
locations[(0, 0)] = 1 # the start position is always visited

# store position x and y of santa
x = 0
y = 0

# read input
moves = open('2015/03/input_a.txt', 'r').readline()
print(moves)

# handle move by move
for c in moves:
    if c == '^':
        y -= 1
    elif c == 'v': 
        y += 1
    elif c == '<':
        x -= 1
    elif c == '>':
        x += 1
    
    locations[(x, y)] += 1

# print the number of unique locations visited
print(len(locations))
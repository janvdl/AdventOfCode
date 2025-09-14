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
santa_x = 0
santa_y = 0
robot_x = 0
robot_y = 0

# read input
moves = open('2015/03/input_a.txt', 'r').readline()
print(moves)

# handle move by move
for i in range(len(moves)):
    real_santa: bool = i % 2 == 0
    c = moves[i]
    
    if c == '^':
        if real_santa:
            santa_y -= 1
        else:
            robot_y -= 1
    elif c == 'v': 
        if real_santa:
            santa_y += 1
        else:
            robot_y += 1
    elif c == '<':
        if real_santa:
            santa_x -= 1
        else:
            robot_x -= 1
    elif c == '>':
        if real_santa:
            santa_x += 1
        else:
            robot_x += 1
    
    if real_santa:
        locations[(santa_x, santa_y)] += 1
    else:
        locations[(robot_x, robot_y)] += 1

# print the number of unique locations visited
print(len(locations))
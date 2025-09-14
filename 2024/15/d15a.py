from enum import Enum
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define directions
class direction(Enum): 
    up    = [-1, 0 ]
    down  = [ 1, 0 ]
    left  = [ 0, -1]
    right = [ 0, 1 ]

# robot
robot_x = 0
robot_y = 0
robot_d = direction.up
    
# import map data and find robot
map = [line.strip() for line in open('input_a_grid.txt', 'r').readlines()]
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == '@':
            print("Found robot at: ", x, y)
            robot_x = x
            robot_y = y

# import move data
moves = list(''.join([line.strip() for line in open('input_a_moves.txt', 'r').readlines()]))

# ============================================

# map print function to monitor the robot
def print_map():
    for i in range(len(map)):
        print(map[i])

# inspect map before starting the rest
clear()
print_map()

# function to replace grid cell values
def grid_mark(map, x, y, c):
    new_grid_line = ''.join(map[x][:y]) + c + ''.join(map[x][y + 1:])
    map[x] = new_grid_line

# recursive function to check whether the move is possible or whether we'll bump into a wall
def can_move(map, x1, y1, x2, y2, d):
    if map[x2][y2] == '.':
        return True # open space
    elif map[x2][y2] == '#':
        return False # wall
    else:
        # move another block ahead and check
        x3 = x2 + d.value[0]
        y3 = y2 + d.value[1]
        return can_move(map, x2, y2, x3, y3, d)
    
# once we know we can move, actually perform the move
def do_move(map, x1, y1, x2, y2, d):
    if map[x2][y2] == '.':
        grid_mark(map, x2, y2, map[x1][y1])
        grid_mark(map, x1, y1, '.')
    else:
        # move the next block first to create space
        x3 = x2 + d.value[0]
        y3 = y2 + d.value[1]
        do_move(map, x2, y2, x3, y3, d) # instruction to move the next block
        do_move(map, x1, y1, x2, y2, d) # come back to this one later

# robot move function
def robot_move(map, x1, y1, d):
    global robot_x, robot_y
    x2 = x1 + d.value[0]
    y2 = y1 + d.value[1]
    if can_move(map, x1, y1, x2, y2, d):
        do_move(map, x1, y1, x2, y2, d)
        robot_x = x2
        robot_y = y2
    print_map()

# calculate the gps total
def calculate_gps_total(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 'O':
                total += (x * 100) + y
    
    return total

# go through each move in the list
while (len(moves)) > 0:
    move = moves.pop(0)
    if move == '<':
        robot_d = direction.left
        print("Moving robot left, if possible")
    elif move == '>':
        robot_d = direction.right
        print("Moving robot right, if possible")
    elif move == '^':
        robot_d = direction.up
        print("Moving robot up, if possible")
    else:
        robot_d = direction.down
        print("Moving robot down, if possible")
    print(len(moves), "instructions remain")
    
    robot_move(map, robot_x, robot_y, robot_d)

# after all the moves have finished, get the gps total
print(calculate_gps_total(map))
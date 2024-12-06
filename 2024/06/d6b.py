from enum import Enum
import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# state of board, if the guard exits or a cycle is found, set halt = True
halted = False
cycle = False

# grid
grid_map_pure = []
grid_map = []
grid_min_x = 0
grid_min_y = 0
grid_max_x = 0
grid_max_y = 0

def print_grid():
    for i in range(len(grid_map)):
        print(grid_map[i])
    print("==========")

# define directions
class direction(Enum): 
    up    = [-1, 0 ]
    down  = [ 1, 0 ]
    left  = [ 0, -1]
    right = [ 0, 1 ]

# guard
guard_start_x = 0
guard_start_y = 0
guard_pos_x = 0
guard_pos_y = 0
guard_direction = direction.up
guard_char = "^"

# record all paths travelled - this way we can work backwards and place obstacles
points_travelled = []

# turn the guard
def guard_turn():
    global guard_direction
    global guard_char

    if guard_direction == direction.up:
        guard_direction = direction.right
        guard_char = ">"
    elif guard_direction == direction.right:
        guard_direction = direction.down
        guard_char = "V"
    elif guard_direction == direction.down:
        guard_direction = direction.left
        guard_char = "<"
    else:
        guard_direction = direction.up
        guard_char = "^"

# peek at next coord
def guard_peek():
    global guard_pos_x
    global guard_pos_y
    new_x = guard_pos_x + guard_direction.value[0]
    new_y = guard_pos_y + guard_direction.value[1]

    if new_x > grid_max_x or new_y > grid_max_y or new_x < grid_min_x or new_y < grid_min_y:
        print("Guard has left map area")
        return None
    else:
        return grid_map[new_x][new_y]

# move the guard
def guard_move():
    global guard_pos_x
    global guard_pos_y
    global halted
    global cycle

    next_block = guard_peek()
    guard_pos = [guard_pos_x, guard_pos_y, guard_direction]

    # check for cycles
    if guard_pos in points_travelled:
        # we have a cycle
        halted = True
        cycle = True
    else:
        points_travelled.append(guard_pos)

    # do the moving bullshit
    if next_block == "#":
        guard_turn()
    elif next_block == "." or next_block == "X":
        # moving is allowed, mark current pos with X
        guard_mark(guard_pos_x, guard_pos_y, "X")
        # move guard and update position
        guard_pos_x += guard_direction.value[0]
        guard_pos_y += guard_direction.value[1]
        guard_mark(guard_pos_x, guard_pos_y, guard_char)
    elif next_block == None:
        guard_mark(guard_pos_x, guard_pos_y, "X")
        halted = True

# mark guard tracks or guard char on map
def guard_mark(x, y, c):
    new_grid_line = ''.join(grid_map[x][:y]) + c + ''.join(grid_map[x][y + 1:])
    grid_map[x] = new_grid_line

# count total number of X's
def count_guard_tracks():
    total = 0
    for line in range(len(grid_map)):
        total += grid_map[line].count("X")

    return total

def reset_guard():
    global guard_pos_x
    global guard_pos_y
    global guard_char
    global guard_direction
    global points_travelled
    global halted
    global cycle
    global grid_map
    global grid_map_pure

    guard_pos_x = guard_start_x
    guard_pos_y = guard_start_y
    guard_char = "^"
    points_travelled.clear()
    halted = False
    cycle = False
    guard_direction = direction.up
    grid_map = grid_map_pure.copy()

# ==========================================
# read input data and parse
with open('input_sample.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
    # set an iterator to find the guard
    currline_index = -1

    for line in lines:
        currline_index += 1
        temp_line = line.replace("\n", "")

        if "^" in temp_line:
            guard_start_x = currline_index
            guard_start_y = temp_line.index("^")

        grid_map.append(temp_line)

    # set constraints
    grid_max_x = len(grid_map[0]) - 1
    grid_max_y = len(grid_map) - 1

    grid_map_pure = grid_map.copy()
    reset_guard()

# start the guard simulation
print_grid()
while not halted:
    print("Guard is at position ", guard_pos_x, ",", guard_pos_y)
    guard_move()
    #print_grid()

# Part A - guard halted, count number of tracks
print("Track count: ", count_guard_tracks())

# Part B - find where extra obstacles will create loops
print("========== Now trying to obstacle placement to create cycles")
potential_obstacles = []
points_travelled_copy = points_travelled.copy() # this will get overwritten as the guard passes through
while len(points_travelled_copy) > 0:
    print("Points to go for evaluating obstacles: ", len(points_travelled_copy))
    # for each point travelled, check if we can induce a cycle by placing an obstacle in the path
    # my logic is: for any point on the path travelled, if we can turn right and find one of our
    #              previous points going in the same direction (without blockers in between) 
    p = points_travelled_copy.pop()

    # reset the guard and place a blocker from the last position on the map, working backwards
    reset_guard()
    guard_mark(p[0], p[1], "#")
    while not halted:
        guard_move()
    
    if cycle:
        obstacle_point = [p[0], p[1]]
        if obstacle_point not in potential_obstacles:
            potential_obstacles.append(obstacle_point)
        print("!! Cycle found by placing obstacle at ", obstacle_point)
    else:
        continue
print(len(potential_obstacles))
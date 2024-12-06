from enum import Enum
import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# state of board, if the guard exits, set halt = True
halted = False

# grid
grid_map = []
grid_min_x = 0
grid_min_y = 0
grid_max_x = 0
grid_max_y = 0

def print_grid():
    for i in range(len(grid_map)):
        print(grid_map[i])

# define directions
class direction(Enum): 
    up    = [-1, 0 ]
    down  = [ 1, 0 ]
    left  = [ 0, -1]
    right = [ 0, 1 ]

# guard
guard_pos_x = 0
guard_pos_y = 0
guard_direction = direction.up
guard_char = "^"

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

    next_block = guard_peek()

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

# ==========================================
# read input data and parse
with open('input_a.txt', 'r') as file:
    lines = file.readlines()
    
    # set an iterator to find the guard
    currline_index = -1

    # set constraints
    grid_max_x = len(lines) - 1
    grid_max_y = len(lines[0]) - 1

    for line in lines:
        currline_index += 1
        temp_line = line.replace("\n", "")

        if "^" in temp_line:
            guard_pos_x = currline_index
            guard_pos_y = temp_line.index("^")
            print("Found guard at", guard_pos_x, ",", guard_pos_y)

        grid_map.append(temp_line)

# start the guard simulation
print_grid()
while not halted:
    print("Guard is at position ", guard_pos_x, ",", guard_pos_y)
    guard_move()
    print_grid()

# guard halted, count number of tracks
print("Track count: ", count_guard_tracks())
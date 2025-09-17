import os
from enum import Enum

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = open('2016/02/input.txt', 'r').readlines()

# keypad
keypad = [
    ['0','0','1','0','0'],
    ['0','2','3','4','0'],
    ['5','6','7','8','9'],
    ['0','A','B','C','0'],
    ['0','0','D','0','0']
]

# directions
class Direction(Enum):
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]

def move_cursor(cursor, direction: Direction):
    cursor_new = [cursor[0] + direction.value[0], cursor[1] + direction.value[1]]
    
    # check for out of bounds
    if cursor_new[0] < 0 or cursor_new[1] < 0 or cursor_new[0] > 4 or cursor_new[1] > 4:
        return cursor
    if keypad[cursor_new[1]][cursor_new[0]] == '0':
        return cursor

    return cursor_new

# process line by line
passcode = ""
cursor = [1, 1]
for line in lines:
    for instr in line.strip():
        if instr == 'U':
            cursor = move_cursor(cursor, Direction.UP)
        elif instr == 'D':
            cursor = move_cursor(cursor, Direction.DOWN)
        elif instr == 'L':
            cursor = move_cursor(cursor, Direction.LEFT)
        else:
            cursor = move_cursor(cursor, Direction.RIGHT)
    passcode += keypad[cursor[1]][cursor[0]]

print(passcode)
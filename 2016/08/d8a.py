import os
import re

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

#====================================================#
#           DEFINE HELPER FUNCTIONS                  #
#====================================================#

def init_screen(screen_width, screen_height):
    screen = [['.' for i in range(screen_width)] for j in range(screen_height)]
    return screen

def print_screen(screen):
    for row in screen:
        for col in row:
            print(col, end='')
        print()
    print()

def rect(screen, x, y):
    for i in range(y):
        for j in range(x):
            screen[i][j] = '#'

    return screen

def rotate_row(screen, index, by):
    '''
    This says "rotate" but it's really just shifting right
    '''

    # grab the current row according to index
    temp_row = screen[index]

    # if we are shifting by x pixels then
    # grab the last x pixels and move them
    # to the front (these are the ones that 'dropped off')
    split1 = temp_row[-1 * by:]
    split2 = temp_row[:-1 * by]
    new_row = split1 + split2

    # replace the original row with the new row
    screen[index] = new_row

    return screen

def rotate_col(screen, index, by):
    '''
    This says "rotate" but it's really just shifting down
    '''

    # grab the current col according to index
    temp_col = [screen[x][index] for x in range(len(screen))]

    # if we are shifting by x pixels then
    # grab the last x pixels and move them
    # to the front (these are the ones that 'dropped off')
    split1 = temp_col[-1 * by:]
    split2 = temp_col[:-1 * by]
    new_col = split1 + split2

    # replace the original col
    for x in range(len(new_col)):
        screen[x][index] = new_col[x]

    return screen

def count_lit(screen):
    lit = 0

    for i in range(len(screen)):
        for j in range(len(screen[i])):
            if screen[i][j] == '#':
                lit += 1

    return lit

#====================================================#
#           END HELPER FUNCTIONS                     #
#====================================================#

# initialise screen area
screen = init_screen(50, 6)

# read input
lines = [l.strip() for l in open('2016/08/input.txt', 'r').readlines()]
for line in lines:
    # parse digits
    numbers = [int(x) for x in re.findall(r"\d+", line)]
    
    # parse instruction
    if 'rect' in line:
        screen = rect(screen, numbers[0], numbers[1])
    if 'column' in line:
        screen = rotate_col(screen, numbers[0], numbers[1])
    if 'row' in line:
        screen = rotate_row(screen, numbers[0], numbers[1])
    
    print(line)
    print_screen(screen)

print(count_lit(screen))
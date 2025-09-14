import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
line = open('2015/01/input_a.txt', 'r').readline().strip()

# read char by char and decide if we're moving up or down
floor = 0
for c in line:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

print(floor)
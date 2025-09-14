import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
line = open('2015/01/input_a.txt', 'r').readline().strip()

# read char by char and find where Santa first enters the basement
floor = 0
for i, c in enumerate(line):
    if c == '(':
        floor += 1
    else:
        floor -= 1
        
    if floor == -1:
        print(i + 1)
        break
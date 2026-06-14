import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#clear()

# index of cursor in array
cursor = 0
steps = 0

# read input
lines = [int(l.strip()) for l in open('2017/05/input.txt', 'r').readlines()]
maxCursor = len(lines)

while cursor < maxCursor:
    steps = steps + 1
    value = lines[cursor]
    lines[cursor] = lines[cursor] + 1
    cursor = cursor + value

print(steps)
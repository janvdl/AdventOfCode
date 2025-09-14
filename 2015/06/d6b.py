import os
import re

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# create 2D array of all lights
lights = [[0 for x in range(1000)] for y in range(1000)]

# read input
lines = [line.strip() for line in open('2015/06/input_a.txt', 'r')]

# read each line with instructions and apply them
for line in lines:
    coord_matches = re.findall(r'\d+', line)
    start_x = int(coord_matches[0])
    start_y = int(coord_matches[1])
    end_x = int(coord_matches[2])
    end_y = int(coord_matches[3])

    if 'turn on' in line:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                lights[x][y] += 1
    elif 'turn off' in line:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                lights[x][y] -= 1 if lights[x][y] > 0 else 0
    elif 'toggle' in line:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                lights[x][y] += 2

# count all lights' brightness levels
count = 0
for x in range(1000):
    for y in range(1000):
        count += lights[x][y]

print(count)
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/02/input_a.txt', 'r')]

# calculate total paper
total = 0
for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    sides = [l*w, w*h, h*l]
    total += (2 * sum(sides)) + min(sides)

print(total)
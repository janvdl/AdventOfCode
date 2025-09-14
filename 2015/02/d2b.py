import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/02/input_a.txt', 'r')]

# calculate total ribbon
total = 0
for line in lines:
    l, w, h = [int(x) for x in line.split('x')]
    bow = l * w * h
    ribbon = 2 * (l + w + h - max(l, w, h)) + bow
    total += ribbon

print(total)
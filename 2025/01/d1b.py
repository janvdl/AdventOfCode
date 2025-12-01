import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2025/01/input.txt', 'r').readlines()]

# keep track of dial and number of zeroes as we loop through the input
dial = 50
zeroes = 0

for l in lines:
    direction = l[0]
    clicks = int(l[1:])
    prev = dial

    for c in range(clicks):
        dial += 1 if direction == 'R' else -1
        if dial == 0 or dial == 100:
            zeroes += 1
            dial = 0
        elif dial == -1:
            dial = 99
        elif dial == 101:
            dial = 1

print(zeroes)
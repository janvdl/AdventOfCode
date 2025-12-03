import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2025/03/input.txt', 'r').readlines()]

# find maximum joltage per line
total_output = 0

for l in lines:
    joltage = 0
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            tmp_joltage = int(l[i] + l[j])
            if tmp_joltage > joltage:
                joltage = tmp_joltage
    total_output += joltage

print(total_output)
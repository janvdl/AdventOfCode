import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/12/input.txt', 'r').readlines()]

# memory register
reg = defaultdict(int)
# part b requires intialising register c to 1
reg['c'] = 1

# process instruction lines
ptr = 0
while (ptr < len(lines)):
    # split instruction into components
    instr = lines[ptr].split()

    if instr[0] == 'cpy':
        if instr[1].isdigit():
            reg[instr[2]] = int(instr[1])
        else:
            reg[instr[2]] = reg[instr[1]]
    elif instr[0] == 'inc':
        reg[instr[1]] += 1
    elif instr[0] == 'dec':
        reg[instr[1]] -= 1
    elif instr[0] == 'jnz':
        if (instr[1].isalpha() and reg[instr[1]] != 0) or (instr[1].isdigit() and int(instr[1]) != 0):
            ptr += int(instr[2])
            continue # do not increment by 1 if we jump

    # advance the instruction pointer for anything but jnz
    ptr += 1

# print final memory register
print(reg)
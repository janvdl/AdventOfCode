
import os
import re
import operator
from functools import reduce

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input and replace multiple spaces with a single space
re_ = re.compile(r"\s+")
lines = [re_.sub(" ", l.strip()).split(" ") for l in open('2025/06/input.txt', 'r').readlines()]

# lambda for add and multiply
add = lambda numbers: reduce(lambda x, y: x + y, numbers, 0)
mul = lambda numbers: reduce(lambda x, y: x * y, numbers, 1)

# process lines
stack = []
total = 0
for col in range(len(lines[0])):
    for row in range(len(lines)):
        tmp = lines[row][col]
        if tmp.isdigit():
            tmp = int(tmp)
        stack.insert(0, tmp)

    op_ = stack.pop(0)

    if op_ == "+":
        total += add(stack)
    elif op_ == "*":
        total += mul(stack)
    stack.clear()

print(total)
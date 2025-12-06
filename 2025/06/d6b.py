
import os
import re
import operator
from functools import reduce
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input and replace multiple spaces with a single space
re_ = re.compile(r"\s+")
lines = [l for l in open('2025/06/input.txt', 'r').readlines()]

# lambda for add and multiply
add = lambda numbers: reduce(lambda x, y: x + y, numbers, 0)
mul = lambda numbers: reduce(lambda x, y: x * y, numbers, 1)

# process lines
total = 0
op_ = ""
stack = []
for col in range(len(lines[0])):
    s = ""
    for row in range(len(lines)):
        tmp = lines[row][col]
        if tmp in ["+", "*"]:
            op_ = tmp
        elif tmp == "\n":
            break
        else:
            s += tmp

    # column string is built, now process    
    s = s.strip()
    if s != "":
        n = int(s)
        stack.append(n)
    else:
        # if the string is empty, we have a blank column, i.e. process and start over
        if op_ == "+":
            total += add(stack)
        elif op_ == "*":
            total += mul(stack)

        op_ = ""
        stack.clear()

print(total)
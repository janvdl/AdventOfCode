import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#clear()

# read input
lines = [l.strip() for l in open('2017/04/input.txt', 'r').readlines()]
count = 0

for l in lines:
    d = defaultdict(int)
    words = l.split()

    for w in words:
        d[''.join(sorted(w))] += 1

    isValid = True
    for k in d:
        if d[k] > 1:
            isValid = False

    if isValid:
        count = count + 1

print(count)
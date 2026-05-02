import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2017/01/input.txt', 'r').readlines()]

for l in lines:
    d = defaultdict(int)
    for i in range(len(l)):
        if l[i] == l[i-1]:
            d[int(l[i])] += 1

    print(d)
    total = 0
    for n in d:
        total += (n * d[n])
    print(total)
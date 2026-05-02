import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#clear()

# read input
lines = [l.strip() for l in open('2017/02/input.txt', 'r').readlines()]
total_diff = 0

for l in lines:
    min = 99999
    max = 0
    for x in l.split():
        n = int(x)
        if n < min:
            min = n
        if n > max:
            max = n
        
    diff = max - min
    total_diff += diff

print(total_diff)
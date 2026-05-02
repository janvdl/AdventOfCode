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
    found = False
    l2 = [int(n) for n in l.split()]
    for i in range(len(l2)):
        if found:
            break
        for j in range(i + 1, len(l2)):
            n1 = l2[i]
            n2 = l2[j]

            if n1 % n2 == 0 or n2 % n1 == 0:
                total_diff += max(n1, n2) // min(n1, n2)
                found = True
                break

print(total_diff)
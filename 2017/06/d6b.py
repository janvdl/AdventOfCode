import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# read input
bank = [int(l.strip()) for l in open('2017/06/input.txt', 'r').readline().split()]
divisor = len(bank) # split across all banks that are not the first instance of max
seen = defaultdict(int)
counter = 0

while tuple(bank) not in seen:
    print(bank)
    seen[tuple(bank)] = counter
    counter += 1

    maxval = max(bank)
    maxidx = bank.index(maxval)
    bank[maxidx] = 0

    while maxval > 0:
        maxidx += 1
        maxidx %= divisor
        maxval -= 1
        bank[maxidx] += 1
else:
    diff = counter - seen[tuple(bank)]
    print(diff)
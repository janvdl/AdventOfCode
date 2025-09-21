import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/06/input.txt', 'r').readlines()]

# message placeholder
message = ''

# process lines
columns = defaultdict(str)
for line in lines:
    for i in range(len(line)):
        columns[i] += line[i]

# process columns
for line in columns.values():
    # char count dictionary
    cc = defaultdict(int)
    for c in line:
        cc[c] += 1

    # most frequent char
    fc = min(cc, key=cc.get)

    # add to message
    message += fc

print(message)
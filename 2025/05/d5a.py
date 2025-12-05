import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
ranges = []
values = []
for l in open('2025/05/input.txt', 'r').readlines():
    if l.strip() != "":
        if '-' in l:
            tmp = l.split("-")
            range_ = (int(tmp[0]), int(tmp[1]))
            ranges.append(range_)
        else:
            tmp = int(l)
            values.append(tmp)

# count spoiled versus fresh
fresh = 0
for v in values:
    for r in ranges:
        if r[0] <= v <= r[1]:
            fresh += 1
            break

print(fresh)
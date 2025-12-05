import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
ranges = []
for l in open('2025/05/input.txt', 'r').readlines():
    if l.strip() != "":
        if '-' in l:
            tmp = l.split("-")
            ranges.append([int(tmp[0]), int(tmp[1])])

# check for overlap
ranges.sort(key=lambda x:x[0])

i = 0
while (i < len(ranges) - 1):
    r0 = ranges.pop(i)
    r1 = ranges.pop(i)

    # check for envelopment
    if (r0[0] <= r1[0] <= r0[1]) and (r0[0] <= r1[1] <= r0[1]):
        ranges.insert(i, r0)
    elif (r1[0] <= r0[0] <= r1[1]) and (r1[0] <= r0[1] <= r1[1]):
        ranges.insert(i, r1)
    # otherwise check if R1S is already in R0
    elif (r0[0] <= r1[0] <= r0[1]):
        r1[0] = r0[1] + 1
        ranges.insert(i, r1)
        ranges.insert(i, r0)
        i = 0
        ranges.sort(key=lambda x:x[0])
    # otherwise check if R0E is already in R1
    elif (r1[0] <= r0[1] <= r1[1]):
        r0[1] = r1[0] - 1
        ranges.insert(i, r1)
        ranges.insert(i, r0)
        i = 0
        ranges.sort(key=lambda x:x[0])
    else:
        ranges.insert(i, r1)
        ranges.insert(i, r0)
        i += 1

fresh = 0
for r in ranges:
    tmp = r[1] - r[0] + 1
    print(f"{r} --> {tmp}")
    fresh += tmp
print(fresh)
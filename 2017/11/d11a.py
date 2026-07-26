import os
from collections import defaultdict

debug = False
if debug:
    steps = "ne,ne,s,s".split(",")
else:
    steps = [l.strip() for l in open('2017/11/input.txt', 'r').readline().split(",")]

# https://www.redblobgames.com/grids/hexagons/ is a fantastic resource

# distance from 0,0,0 to q,r,s is (q + r + s) / 2 (q,r,s must be absolute vals)
def hexdist(q, r, s):
    dist = (abs(q) + abs(r) + abs(s)) / 2
    return dist

# implement cube coordinates
q = 0
r = 0
s = 0

for step in steps:
    if step == 'n':
        s += 1
        r -= 1
    elif step == 'nw':
        s += 1
        q -= 1
    elif step == 'ne':
        q += 1
        r -= 1
    elif step == 's':
        s -= 1
        r += 1
    elif step == 'sw':
        q -= 1
        r += 1
    elif step == 'se':
        q += 1
        s -= 1
    else:
        print("E-R-R-O-R:", step)

print(hexdist(q, r, s))
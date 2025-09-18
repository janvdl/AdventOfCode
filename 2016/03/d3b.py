import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = open('2016/03/input.txt', 'r').readlines()

# process lines
valid_triangles = 0

chunk = []

while len(lines) > 0:
    while len(chunk) < 3:
        chunk.append([int(n) for n in lines.pop(0).strip().split()])
    
    for x in range(3):
        a = chunk[0][x]
        b = chunk[1][x]
        c = chunk[2][x]
        if (a + b > c) and (b + c > a) and (a + c > b):
            valid_triangles += 1

    # reset the chunk
    chunk = []

print(valid_triangles)
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = open('2016/03/input.txt', 'r').readlines()

# process lines
valid_triangles = 0
for line in lines:
    vals = [int(x) for x in line.strip().split()]
    a = vals[0]
    b = vals[1]
    c = vals[2]
    valid_triangles += 1 if (a + b > c) and (b + c > a) and (a + c > b) else 0

print(valid_triangles)
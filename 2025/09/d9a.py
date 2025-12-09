import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# function to calculate area
def area(p, q):
    w = p[0] - q[0] + 1
    h = p[1] - q[1] + 1
    return abs(h * w)

# read input
points = []
for l in open('2025/09/input.txt', 'r').readlines():
    x, y = map(int, l.strip().split(","))
    p = (x, y)
    points.append(p)

# naive solution is just to brute force each area
# with the benefit of time, you could probably split the coords into quadrants

max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p = points[i]
        q = points[j]

        tmp_area = area(p, q)
        if tmp_area > max_area:
            max_area = tmp_area

print(max_area)
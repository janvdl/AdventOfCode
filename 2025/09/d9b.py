import os
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, box

# usually I do not do "import <solution>" 
# but I prefer this over writing my own Polygon handler

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# function to calculate area
def area(p, q):
    w = abs(p[0] - q[0]) + 1
    h = abs(p[1] - q[1]) + 1
    return h * w

# function to check if rectangle is contained 
# within death star polygon
def is_valid(poly, p, q) -> bool:
    x_min = min(x[0] for x in [p, q])
    x_max = max(x[0] for x in [p, q])
    y_min = min(x[1] for x in [p, q])
    y_max = max(x[1] for x in [p, q])

    r = box(x_min, y_min, x_max, y_max)

    if poly.covers(r):
        return True
    else:
        return False

# read input
points = []
for l in open('2025/09/input.txt', 'r').readlines():
    x, y = map(int, l.strip().split(","))
    p = [x, y]
    points.append(p)

# death star polygon
poly = Polygon(points)

# brute forcing it again
max_area = 0
max_p = None
max_q = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if i == j:
            continue

        p = points[i]
        q = points[j]

        if is_valid(poly, p, q):
            tmp_area = area(p, q)
            if tmp_area > max_area:
                max_area = tmp_area
                max_p = p
                max_q = q

print(max_area)

# death star plot
points.append(points[0])
x = [p[0] for p in points]
y = [p[1] for p in points]
plt.plot(x, y, 'b')
plt.plot(max_p[0], max_p[1], 'o') # rectangle corners
plt.plot(max_q[0], max_q[1], 'o') # rectangle corners
plt.plot(max_p[0], max_q[1], 'o')
plt.plot(max_q[0], max_p[1], 'o')
plt.text(0, 0, "Area: " + str(max_area))
plt.show()
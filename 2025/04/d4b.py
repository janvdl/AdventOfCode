import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [list(l.strip()) for l in open('2025/04/input.txt', 'r').readlines()]

# function to count adjacent rolls of paper
def is_accessible(gridmap, x, y) -> bool:
    count: int = 0

    can_go_left: bool = x > 0
    can_go_right: bool = x < len(gridmap[0]) - 1
    can_go_up: bool = y > 0
    can_go_down: bool = y < len(gridmap) - 1

    # check cross formation
    if can_go_left:
        count += 1 if gridmap[y][x - 1] == "@" else 0
    if can_go_right:
        count += 1 if gridmap[y][x + 1] == "@" else 0
    if can_go_up:
        count += 1 if gridmap[y - 1][x] == "@" else 0
    if can_go_down:
        count += 1 if gridmap[y + 1][x] == "@" else 0
    
    # check diagonals
    if can_go_left and can_go_up:
        count += 1 if gridmap[y - 1][x - 1] == "@" else 0
    if can_go_left and can_go_down:
        count += 1 if gridmap[y + 1][x - 1] == "@" else 0
    if can_go_right and can_go_up:
        count += 1 if gridmap[y - 1][x + 1] == "@" else 0
    if can_go_right and can_go_down:
        count += 1 if gridmap[y + 1][x + 1] == "@" else 0

    return count < 4

# process lines as a gridmap
def find_moveable_rolls(lines) -> int:
    moveable_rolls: int = 0
    points_to_remove = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@" and is_accessible(lines, x, y):
                moveable_rolls += 1
                points_to_remove.append((x, y))

    return moveable_rolls, points_to_remove

# initial call
total_moveable_count: int = 0
count, points = find_moveable_rolls(lines)
while count > 0:
    total_moveable_count += count
    for p in points:
        lines[p[1]][p[0]] = "."

    count, points = find_moveable_rolls(lines)

print(total_moveable_count)
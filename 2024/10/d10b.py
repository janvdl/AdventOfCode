import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# grid constraints
grid_max_x = 0
grid_max_y = 0

# locations of zeroes
zeroes = []

# import data
grid  = [list(map(int, list(line.strip()))) for line in open('input_a.txt', 'r').readlines()]
grid_max_x = len(grid) - 1
grid_max_y = len(grid[0]) - 1
print(grid)

# dfs to traverse paths
def dfs(s, x, y):
    if x < 0 or x > grid_max_x or y < 0 or y > grid_max_y:
        return 0 # outside of bounds
    else:
        c = grid[x][y]
        if c <= s or abs(c - s) >= 2:
            return 0 # current value is smaller than previous value, we have to move higher and higher by 1 only
        elif c == 9:
            print("Reached a summit at", x, y)
            return 1 # we have reached a 9
        else:
            print("Navigating on from", x, y, "with value", c)
            return dfs(c, x - 1, y) + dfs(c, x + 1, y) + dfs(c, x, y - 1) + dfs(c, x, y + 1)

# find zeroes
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 0:
            zeroes.append([x, y])

# add up all the scores
total = 0
for zero in zeroes:
    print("=============== Starting at", zero[0], zero[1])
    score = dfs(-1, zero[0], zero[1])
    total += score
print(total)
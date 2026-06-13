import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#clear()

# define input
input = 277678

# define moves, they increase by 2 each time they recur
# Right 1
# Up    1
# Left  2
# Down  2
# Right 3
# Up    3
# Left  4
# Down  4
# ...
movecounts = {"R": 1, "U": 1, "L": 2, "D": 2}
moves = ["R", "U", "L", "D"]

# function to calculate nextval
def calcNext(G, x, y):
    next = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                next += G[(x+i, y+j)]
    
    G[(x, y)] = next

# Grid (x, y)
x = 0
y = 0
G = defaultdict(int)
G[(0, 0)] = 1

isSolved = False

while not isSolved:
    move = moves.pop(0)
    moves.append(move)

    for i in range(movecounts[move]):
        if move == "R":
            x = x + 1
        elif move == "U":
            y = y + 1
        elif move == "L":
            x = x - 1
        else:
            y = y - 1

        calcNext(G, x, y)
        print(x, y, G[(x, y)])
        if G[(x, y)] > input:
            isSolved = True
            print(G[(x, y)])
            break

    movecounts[move] = movecounts[move] + 2
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
line = open('2016/01/input.txt', 'r').readline().strip()
#line = 'R8, R4, R4, R8'
instructions = [x.strip() for x in line.split(',')]

# steps dict
steps = { 'N': 0, 'E': 0, 'S': 0, 'W': 0 }
curr_orientation = 0
orientation = ['N', 'E', 'S', 'W']

def change_orientation(go_left: bool):
    global curr_orientation
    if go_left:
        if curr_orientation == 0:
            curr_orientation = 3
        else: 
            curr_orientation -= 1
    else:
        if curr_orientation == 3:
            curr_orientation = 0
        else:
            curr_orientation += 1

# keep track of blocks visited
pos = [0, 0]
hist = []
block_count = 0
cross_over = False

# process instructions
for instr in instructions:
    block_count += 1
    go_left = (instr[0] == 'L')
    step_count = int(instr[1:])

    change_orientation(go_left)
    steps[orientation[curr_orientation]] += step_count

    for x in range(step_count):
        if orientation[curr_orientation] == 'N':
            pos[1] -= 1
        elif orientation[curr_orientation] == 'S':
            pos[1] += 1
        elif orientation[curr_orientation] == 'W':
            pos[0] -= 1
        elif orientation[curr_orientation] == 'E':
            pos[0] += 1

        if pos in hist:
            cross_over = True
            break
        else:
            hist.append(pos[:])

    if cross_over:
        break

    distance = abs(steps['N'] - steps['S']) + abs(steps['W'] - steps['E'])
    print('Turning', 'L' if go_left else 'R', 'to cardinal', orientation[curr_orientation], 'for', step_count, 'steps with current distance at', distance)

print('Crossed paths at pos', pos, 'with distance', abs(pos[0]) + abs(pos[1]))
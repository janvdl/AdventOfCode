import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
line = open('2016/01/input.txt', 'r').readline().strip()
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

# process instructions
for instr in instructions:
    go_left = (instr[0] == 'L')
    step_count = int(instr[1:])

    change_orientation(go_left)
    steps[orientation[curr_orientation]] += step_count
    distance = abs(steps['N'] - steps['S']) + abs(steps['W'] - steps['E'])
    print('Turning', 'L' if go_left else 'R', 'to cardinal', orientation[curr_orientation], 'for', step_count, 'steps with current distance at', distance)

print(steps)
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
output = ''
line = open('2016/09/input.txt', 'r').readline().strip()
#line = 'X(8x2)(3x3)ABCY'

marker_open = False
marker_x = False
marker_len = ''
marker_rep = ''
i = 0
while i < len(line):
    # open paren indicates the start of a marker
    if line[i] == '(':
        marker_open = True

        # reset markers
        marker_x = False
        marker_len = ''
        marker_rep = ''
        i += 1
    # close paren indicates the end of a marker, so process 
    # len and rep and move the cursor (i) forward
    elif line[i] == ')':
        marker_open = False
        temp = line[i + 1 : i + int(marker_len) + 1] * int(marker_rep)
        output += temp
        i += int(marker_len) + 1
    # x indicates shifting from len to rep
    elif line[i] == 'x':
        marker_x = True
        i += 1
    else:
        # marker is open, but before x: len
        if marker_open and not marker_x:
            marker_len += line[i]
            i += 1
        # marker is open, and after x: rep
        elif marker_open and marker_x:
            marker_rep += line[i]
            i += 1
        # normal character, no markers, just output
        elif not marker_open:
            output += line[i]
            i += 1

print(len(output))
import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/04/input.txt', 'r').readlines()]

for line in lines:
    line_split = line.split('[')
    
    # get the 3 components of each room code separately
    encrypted_name = ''.join([c for c in line_split[0] if c.isalpha()])
    sector_id = int(''.join([n for n in line_split[0] if n.isdigit()]))
    checksum = ''.join([c for c in line_split[1] if c.isalpha()])

    # shift the room name by sector_id number of rotations
    shifted_name = ''
    for c in encrypted_name:
        t1 = ord(c)
        t2 = t1 + (sector_id % 26)
        while t2 > 122:
            t2 -= 26
        t3 = chr(t2)
        shifted_name += t3
    
    if 'north' in shifted_name:
        print(encrypted_name, ':', shifted_name, ':', sector_id)

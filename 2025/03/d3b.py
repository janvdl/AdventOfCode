import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2025/03/input.txt', 'r').readlines()]

# find maximum joltage per line
total_output = 0

for l in lines:
    tmp_l = l[:]
    i = 0
    while len(tmp_l) > 12:
        x, y = int(tmp_l[i]), int(tmp_l[i + 1])
        if y > x:
            tmp_l = tmp_l[:i] + tmp_l[i+1:]
            i = 0
        else:
            i += 1
            if i == len(tmp_l) - 1:
                tmp_l = tmp_l[:12]
                break
    
    joltage = int(tmp_l)
    total_output += joltage
    

print(total_output)
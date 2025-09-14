from collections import defaultdict
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/05/input_a.txt', 'r')]

# check which strings are naughty or nice
# make a list and check it twice
nice_count = 0
for line in lines:
    rule1 = False
    rule2 = False

    # check for double pairs
    for i in range(len(line) - 2):
        substr = line[i:i+2]
        for j in range(i+2, len(line) - 1):
            substr2 = line[j:j+2]
            if substr == substr2:
                rule1 = True
                break

        # check for repeating letter with one letter in between
        k = i + 2
        if line[i] == line[k]:
            rule2 = True

    # check if both rules are satisfied
    if rule1 and rule2:
        nice_count += 1

print(nice_count)
import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

input = [l.strip() for l in open('2017/09/input.txt', 'r').readlines()][0]
#print(input)

#input = "{<{},{},{{}}>}"
total = 0

brace_counter = 0
garbage = False
negation = False

for c in input:
    if not negation:
        if c == "!":
            negation = True
            continue
        elif c == "<" and not garbage: 
            garbage = True
        elif c == ">":
            garbage = False
        elif c == "{" and not garbage:
            brace_counter += 1
        elif c == "}" and not garbage:
            total += brace_counter
            brace_counter -= 1
    else:
        negation = False

print(total)
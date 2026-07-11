import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

input = [l.strip() for l in open('2017/09/input.txt', 'r').readlines()][0]
#print(input)

#input = "<<<<>"

garbage = False
garbage_counter = 0
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
            pass
        elif c == "}" and not garbage:
            pass
        elif garbage:
            garbage_counter += 1
    else:
        negation = False

print(garbage_counter)
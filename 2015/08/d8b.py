import os
import re

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/08/input_a.txt', 'r')]

# count characters per line and escape as necessary
char_count = 0
for line in lines:
    encoded = re.escape(line)
    encoded = encoded.replace('"', '\\"')
    diff = (len(encoded) + 2) - len(line) # remember to add 2 for the quotes that should be surrounding the encoded string
    char_count += diff

    print(f'{line} -> {encoded} ({diff})')

print(char_count)
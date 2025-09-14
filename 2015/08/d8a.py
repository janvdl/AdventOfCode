import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [line.strip() for line in open('2015/08/input_a.txt', 'r')]

# count characters per line and escape as necessary
char_count = 0
for line in lines:
    decoded = bytes(line, 'utf-8').decode('unicode_escape')
    diff = len(line) - (len(decoded) - 2) # remember to subtract 2 for the quotes surrounding the decoded string
    char_count += diff

    print(f'{line} -> {decoded} ({diff})')

print(char_count)
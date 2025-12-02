import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# function to check for repeated digits
def no_repeats(s):
    first_half  = s[:len(s)//2]
    second_half = s[len(s)//2:]

    if first_half == second_half:
        return False
    
    return True

# read input
line = open('2025/02/input.txt', 'r').readline().strip()
ranges = line.split(',')

total_invalid = 0
for r in ranges:
    bounds = r.split('-')
    start, end = int(bounds[0]), int(bounds[1])

    for n in range(start, end + 1):
        if not no_repeats(str(n)):
            print(f"Has repeated digits: {str(n)}")
            total_invalid += n

print(total_invalid)
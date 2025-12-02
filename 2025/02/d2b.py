import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# function to find divisors
# this will be used to split the string into even chunks
def divisors(n):
    divisors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0: 
            divisors.append(i)
    return divisors

# function to check for repeated digits
def no_repeats(s):
    l = len(s)
    chunk_sizes = divisors(l)
    valid = True

    for chunk_size in chunk_sizes:
        chunks = []
        for i in range(0, len(s), chunk_size):
            chunks.append(s[i:i + chunk_size])

        if all(c == chunks[0] for c in chunks):
            valid = False
            break

    return valid

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
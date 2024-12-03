import re

total = 0

with open('input_a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # regex to extract the mul() statement
        mul_matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        for match in mul_matches:
            total += int(match[0]) * int(match[1])

print(total)
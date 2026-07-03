import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# registers
cpu = defaultdict(int)

# read nodes
lines = [l.strip().split() for l in open('2017/08/input.txt', 'r').readlines()]
for l in lines:
    register = l[0]
    operation = l[1]
    value = int(l[2])
    condition_register = l[4]
    condition_operator = l[5]
    condition_value = int(l[6])

    if condition_operator == "==":
        if cpu[condition_register] == condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)

    if condition_operator == ">":
        if cpu[condition_register] > condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)

    if condition_operator == "<":
        if cpu[condition_register] < condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)

    if condition_operator == ">=":
        if cpu[condition_register] >= condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)

    if condition_operator == "<=":
        if cpu[condition_register] <= condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)

    if condition_operator == "!=":
        if cpu[condition_register] != condition_value:
            cpu[register] += value if operation == 'inc' else (value * -1)
    
    print(cpu)

max_register = 0
for register in cpu:
    if cpu[register] > max_register:
        max_register = cpu[register]

print("max value:", max_register)
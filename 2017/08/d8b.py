import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# registers
cpu = defaultdict(int)
cpu["__max"] = 0

def update_register(cpu, register, operation, value):
    cpu[register] += value if operation == 'inc' else (value * -1)
    if cpu[register] > cpu["__max"]:
        cpu["__max"] = cpu[register]

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
            update_register(cpu, register, operation, value)

    if condition_operator == ">":
        if cpu[condition_register] > condition_value:
            update_register(cpu, register, operation, value)

    if condition_operator == "<":
        if cpu[condition_register] < condition_value:
            update_register(cpu, register, operation, value)

    if condition_operator == ">=":
        if cpu[condition_register] >= condition_value:
            update_register(cpu, register, operation, value)

    if condition_operator == "<=":
        if cpu[condition_register] <= condition_value:
            update_register(cpu, register, operation, value)

    if condition_operator == "!=":
        if cpu[condition_register] != condition_value:
            update_register(cpu, register, operation, value)
    
    print(cpu)

print("max value:", cpu["__max"])
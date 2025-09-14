from collections import defaultdict
import os
import math
import re

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define registers
registers = defaultdict(int)
registers['A'] = 0
registers['B'] = 0
registers['C'] = 0

# read input and populate registers
lines = [line.strip() for line in open('2024/17/input_a.txt', 'r').readlines()]

num_matches = re.findall(r'\d+', lines.pop(0))
registers['A'] = int(num_matches[0])
num_matches = re.findall(r'\d+', lines.pop(0))
registers['B'] = int(num_matches[0])
num_matches = re.findall(r'\d+', lines.pop(0))
registers['C'] = int(num_matches[0])

tape = []
num_matches = re.findall(r'\d+', lines.pop())
for match in num_matches:
    tape.append(int(match))

print(tape)
# ================================#
# machine & opcode specifications #
# ================================#
# 0: adv : bitwise shift value of register A by operand and write to A
# 1: bxl : bitwise xor value of register B by operand and write to B
# 2: bst : mod 8 of operand and write to B
# 3: jnz : if register A is 0, do nothing, otherwise move instruction pointer to operand value
# 4: bxc : bitwise XOR of registers B and C and write result to B; it does read an operand (i.e., moves the instruction pointer fwds) but ignores it
# 5: out : calculates value of operand mod 8 and outputs it
# 6: bdv : bitwise shift value of register A by operand and write to B (basically opcode 0 but writes to B)
# 7: cdv : bitwise shift value of register A by operand and write to C (basically opcode 0 but writes to C)

def run_machine(registers, tape):
    ptr = 0
    output = []
    while ptr < len(tape):
        # get opcode and operand
        opcode = tape[ptr]
        ptr += 1
        operand = tape[ptr]
        lit_operand = operand

        # interpret operand to check if we're referring to registers
        if operand == 4:
            operand = registers['A']
        elif operand == 5:
            operand = registers['B']
        elif operand == 6:
            operand = registers['C']
        

        if opcode == 0:
            registers['A'] = registers['A'] >> operand
        elif opcode == 1:
            registers['B'] = registers['B'] ^ lit_operand
        elif opcode == 2:
            registers['B'] = operand % 8
        elif opcode == 3:
            if registers['A'] != 0:
                ptr = lit_operand
                continue
        elif opcode == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:
            output.append(operand % 8)
        elif opcode == 6:
            registers['B'] = registers['A'] >> operand
        elif opcode == 7:
            registers['C'] = registers['A'] >> operand

        ptr += 1

    return output

output = run_machine(registers, tape)
print(output)
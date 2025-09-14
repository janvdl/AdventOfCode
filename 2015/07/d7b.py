import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define register
register = {}
register['b'] = 16076

# read input
instructions = [line.strip() for line in open('2015/07/input_a.txt', 'r')]

def can_process(instruction, register):
    # check if instruction can be processed
    references = instruction.split('->')[0].split()
    destination = instruction.split('->')[1].strip()

    if destination in register:
        return False # already processed, don't overwrite B since we hardwired it above

    if len(references) == 1:
        ref = references[0]
        if ref in register or ref.isdigit():
            return True
    elif len(references) == 2:
        ref = references[1]
        if ref in register or ref.isdigit():
            return True
    else:
        ref1 = references[0]
        ref2 = references[2]
        if (ref1 in register or ref1.isdigit()) and (ref2 in register or ref2.isdigit()):
            return True

    return False

def do_process(instruction, register):
    # process instruction
    destination = instruction.split('->')[1].strip()
    references = instruction.split('->')[0].split()

    if len(references) == 1:
        ref = references[0]
        op = ref if ref.isdigit() else register[ref]
        register[destination] = int(op)
    elif len(references) == 2:
        gate = references[0]
        ref = references[1]
        op = ref if ref.isdigit() else register[ref]
        op = int(op)

        if gate == 'NOT':
            register[destination] = ~op
            if register[destination] < 0:
                register[destination] = 65536 + register[destination]
    else:
        gate = references[1]
        ref1 = references[0]
        ref2 = references[2]

        op1 = ref1 if ref1.isdigit() else register[ref1]
        op2 = ref2 if ref2.isdigit() else register[ref2]
        op1 = int(op1)
        op2 = int(op2)

        if gate == 'AND':
            register[destination] = op1 & op2
        elif gate == 'OR':
            register[destination] = op1 | op2
        elif gate == 'LSHIFT':  
            register[destination] = op1 << op2
        elif gate == 'RSHIFT':
            register[destination] = op1 >> op2
        else:
            print('Invalid gate:', gate)

# process instructions
# this is a bit hacky, because there will always be one instruction left, namely the one that assigns to B
while len(instructions) > 1:
    instruction = instructions.pop(0)

    if can_process(instruction, register):
        do_process(instruction, register)
    else:
        instructions.append(instruction)

# evaluate register of signals
print(register)
print(register['a'])
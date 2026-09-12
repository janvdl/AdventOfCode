import os
from collections import defaultdict

# generate list of chars from a to ...
def genChars(start, end):
    chars = [chr(c) for c in range(ord(start), ord(end) + 1)]
    return chars

# init variables
debug = False
line = None
chars = []
programs = defaultdict(int)

# read input
if debug:
    line = open('2017/16/input_sample.txt', 'r').readline()
    chars = genChars('a', 'e')
else:
    line = open('2017/16/input.txt', 'r').readline()
    chars = genChars('a', 'p')

# initialise the programs dictionary by populating:
#   programs[a] = 0
#   programs[b] = 1 ...
for i, v in enumerate(chars):
    programs[v] = i

# functions to perform spin, exchange, partner
def spin(programs, x):
    l = len(programs)
    for k in programs:
        # add x to each program's recorded position and mod to shift the ones at the end to the start
        programs[k] += x 
        programs[k] %= l

def exchange(programs, a, b):
    # exchange looks at numerical positions
    # generate reverse dictionary for lookups
    programs_rev = {v: k for k, v in programs.items()}
    a_ = programs_rev[a]
    b_ = programs_rev[b]

    # now that we know the programs at positions a and b, we can pass their names (a_ and b_) to partner to swap them
    partner(programs, a_, b_)
    
def partner(programs, a, b):
    # partner looks at alphabetical names of programs and swaps them
    programs[a], programs[b] = programs[b], programs[a]

# loop over instructions
instrs = line.split(',')
for instr in instrs:
    command, params = instr[0], instr[1:]
    if command == 's':
        spin(programs, int(params))
    elif command == 'x':
        params_ = params.split('/')
        exchange(programs, int(params_[0]), int(params_[1]))
    elif command == 'p':
        params_ = params.split('/')
        partner(programs, params_[0], params_[1])
    else:
        print("E-R-R-O-R")

# after all instructions have been executed get the order of programs from 0 to ...
# create dictionary reverse lookup
programs_rev = {v: k for k, v in programs.items()}

for x in range(0, len(programs_rev)):
    print(programs_rev[x], end="")
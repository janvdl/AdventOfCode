### Not a valid solution ###

import os
from collections import defaultdict
import d23_helpers

# init dictionary for registers
register = defaultdict(int)

# read input
debug = False
lines = None
if debug:
    lines = open('2017/23/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/23/input.txt', 'r').readlines()

register['line'] = 0 # initialise to line 0 of the program (i.e., what's contained in lines)
register['maxlines'] = len(lines)
register['halt'] = 0

# for part b, register['a'] should be initialised to 1
register['a'] = 1

# program execution
while register['halt'] == 0:
    instr = lines[register['line']].strip()
    print(f"{register['line']}: {instr}")
    d23_helpers.parse(register, instr)
    print("  ".join(f"{r} = {register[r]:>+8}" for r in "abcdefgh"))
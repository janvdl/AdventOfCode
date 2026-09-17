import os
from collections import defaultdict

# read input
debug = False
lines = None
if debug:
    lines = open('2017/18/input_sample2.txt', 'r').readlines()
else:
    lines = open('2017/18/input.txt', 'r').readlines()

def create_register(programnum: int):
    # initialise register with program num
    register = defaultdict(int)
    register['p'] = programnum
    register['line'] = 0 # initialise to line 0 of the program (i.e., what's contained in lines)
    register['snd'] = 0
    register['sndcount'] = 0 # count how many values were sent
    register['halt'] = 0
    register['pause'] = 0

    # initialise a buffer for the send/receive of values between programs
    buffer = []

    return register, buffer

# functions to operate on registers
def reg_set(r, x, y):
    r[x] = reg_get(r, y)
    r['line'] += 1

def reg_get(r, y) -> int:
    try:
        tmp = int(y)
        return tmp
    except ValueError:
        return r[y]

def reg_add(r, x, y):
    r[x] += reg_get(r, y)
    r['line'] += 1

def reg_mul(r, x, y):
    r[x] *= reg_get(r, y)
    r['line'] += 1

def reg_mod(r, x, y):
    r[x] %= reg_get(r, y)
    r['line'] += 1

def reg_rcv(r, b, x):
    if len(b) > 0:
        r[x] = b.pop(0)
        r['pause'] = 0 # unpause, we can continue parsing lines
        r['line'] += 1
    else:
        r['pause'] = 1 # wait for data

def reg_jgz(r, x, y):
    if reg_get(r, x) > 0:
        r['line'] += reg_get(r, y)
    else:
        r['line'] += 1

def reg_snd(r, b, x):
    b.append(reg_get(r, x))
    r['sndcount'] += 1
    r['line'] += 1

def parse(r, snd_buf, rcv_buf, instr):
    # split instruction line and parse
    parts = instr.split(' ')
    comm = parts[0]
    x = parts[1]
    y = None
    if len(parts) == 3:
        y = parts[2]

    if comm == "set":
        reg_set(r, x, y)
    elif comm == "add":
        reg_add(r, x, y)
    elif comm == "mul":
        reg_mul(r, x, y)
    elif comm == "mod":
        reg_mod(r, x, y)
    elif comm == "rcv":
        reg_rcv(r, rcv_buf, x)
    elif comm == "jgz":
        reg_jgz(r, x, y)
    elif comm == "snd":
        reg_snd(r, snd_buf, x)
    else:
        r['halt'] = 1
        print("E-R-R-O-R")
    

# program execution
r0, b0 = create_register(0)
r1, b1 = create_register(1)

while r0['halt'] == 0 or r1['halt'] == 0:
    if r0['halt'] == 0:
        instr = lines[r0['line']].strip()
        parse(r0, b1, b0, instr)

    if r1['halt'] == 0:
        instr = lines[r1['line']].strip()
        parse(r1, b0, b1, instr)

    if r0['pause'] == 1 and r1['pause'] == 1:
        r0['halt'] = 1
        r1['halt'] = 1

print(r1['sndcount'])
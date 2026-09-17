import os
from collections import defaultdict

# init dictionary for registers
register = defaultdict(int)

# read input
debug = False
lines = None
if debug:
    lines = open('2017/18/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/18/input.txt', 'r').readlines()

register['line'] = 0 # initialise to line 0 of the program (i.e., what's contained in lines)
register['snd'] = 0
register['halt'] = 0

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

def reg_rcv(r, x):
    tmp = reg_get(r, x)
    if tmp != 0:
        print(r['snd'])
        r['halt'] = 1 # part A requires the program to halt when the first non-zero rcv is executed
    else:
        r['line'] += 1

def reg_jgz(r, x, y):
    if r[x] > 0:
        r['line'] += reg_get(r, y)
    else:
        r['line'] += 1

def reg_snd(r, x):
    register['snd'] = reg_get(r, x)
    r['line'] += 1

def parse(r, instr):
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
        reg_rcv(r, x)
    elif comm == "jgz":
        reg_jgz(r, x, y)
    elif comm == "snd":
        reg_snd(r, x)
    else:
        r['halt'] == 1
        print("E-R-R-O-R")
    

# program execution
while register['halt'] == 0:
    instr = lines[register['line']].strip()
    parse(register, instr)
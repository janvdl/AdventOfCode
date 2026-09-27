# functions to operate on registers
def inc_line(r, v = 1):
    r['line'] += v
    if r['line'] >= r['maxlines']:
        r['halt'] = 1

def reg_set(r, x, y):
    r[x] = reg_get(r, y)
    inc_line(r)

def is_int(y) -> bool:
    try:
        tmp = int(y)
        return True
    except ValueError:
        return False

def reg_get(r, y) -> int:
    if is_int(y):
        return int(y)
    else:
        return r[y]

def reg_add(r, x, y):
    if not is_int(x):
        r[x] += reg_get(r, y)
    inc_line(r)

def reg_sub(r, x, y):
    if not is_int(x):
        r[x] -= reg_get(r, y)
    inc_line(r)

def reg_mul(r, x, y):
    if not is_int(x):
        r[x] *= reg_get(r, y)
    inc_line(r)
    r['mul_counter'] += 1 # explicit ask for part A

def reg_mod(r, x, y):
    if not is_int(x):
        r[x] %= reg_get(r, y)
    inc_line(r)

def reg_jgz(r, x, y):
    tmp = int(x) if is_int(x) else r[x]
    if tmp > 0:
        inc_line(r, reg_get(r, y))
    else:
        inc_line(r)

def reg_jnz(r, x, y):
    tmp = int(x) if is_int(x) else r[x]
    if tmp != 0:
        inc_line(r, reg_get(r, y))
    else:
        inc_line(r)

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
    elif comm == "sub":
        reg_sub(r, x, y)
    elif comm == "mul":
        reg_mul(r, x, y)
    elif comm == "mod":
        reg_mod(r, x, y)
    elif comm == "jgz":
        reg_jgz(r, x, y)
    elif comm == "jnz":
        reg_jnz(r, x, y)
    else:
        r['halt'] = 1
        print("E-R-R-O-R")
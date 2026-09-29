import os
from collections import defaultdict

# init tape, cursor (tape index) will determine value
tape = defaultdict(int)

# function to read current state and indicate next state
def turing(tape, state, cursor):
    if state == "A":
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "B"
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = "C"
    elif state == "B":
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "A"
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = "D"
    elif state == "C":
        if tape[cursor] == 0:
            tape[cursor] = 0
            cursor -= 1
            state = "B"
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = "E"
    elif state == "D":
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "A"
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = "B"
    elif state == "E":
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "F"
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor -= 1
            state = "C"
    elif state == "F":
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "D"
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = "A"
    else:
        raise NotImplementedError
    
    return state, cursor

state = "A"
cursor = 0
for i in range(12667664):
    state, cursor = turing(tape, state, cursor)

print(sum(tape.values()))
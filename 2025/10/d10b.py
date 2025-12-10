import os
import z3

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input and process
presses = 0
for l in open('2025/10/input.txt', 'r').readlines():
    problem = l.split()
    # remove unnecessary brackets and braces
    for t in range(len(problem)):
        problem[t] = problem[t][1:-1]

    # get buttons and joltage
    buttons = [[int(c) for c in button_press.split(",")] for button_press in problem[1:-1]]
    joltage = [int(c) for c in problem[-1].split(",")]
    
    len_b = len(buttons)
    len_j = len(joltage)

    var = [z3.Int(i) for i in range(len_b)]
    eqs = [(z3.Sum([var[j] for j in range(len_b) if i in buttons[j]]) == joltage[i]) for i in range(len_j)]

    opt = z3.Optimize()
    opt.add(*[x >= 0 for x in var], *eqs)
    opt.minimize(z3.Sum(var))
    assert opt.check() == z3.sat
    model = opt.model()

    presses += sum(model[x].as_long() for x in var)

print(presses)
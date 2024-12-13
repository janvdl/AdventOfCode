import os
import re

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# define button costs
cost_A = 3
cost_B = 1

# import data
data  = [line.strip() for line in open('input_a.txt', 'r').readlines() if line.strip() != '']

# extract digits from line
def extractDigits(line):
    num_matches = re.findall(r'\d+', line)
    return num_matches

# today's problem is just a set of simultaneous equations
# Px = a(Ax) + b(Bx)    .... (1)
# Py = a(Ay) + b(By)    .... (2)
#
# Isolate a in (1)
# a = (Px - (b * Bx)) / Ax
# Then substitute a in (2) and isolate b
# b = ((Ax * Py) - (Ay * Px)) / ((By * Ax) - (Bx * Ay))

# run every 3 lines to find coords
total_cost = 0
while len(data) > 0:
    # parse data
    line_A = data.pop(0)
    line_A_digits = extractDigits(line_A)
    line_B = data.pop(0)
    line_B_digits = extractDigits(line_B)
    line_P = data.pop(0)
    line_P_digits = extractDigits(line_P)

    # populate variables for solving
    Ax = int(line_A_digits[0])
    Ay = int(line_A_digits[1])
    Bx = int(line_B_digits[0])
    By = int(line_B_digits[1])
    Px = int(line_P_digits[0])
    Py = int(line_P_digits[1])

    # solve number of presses for buttons A and B
    b = ((Ax * Py) - (Ay * Px)) / ((By * Ax) - (Bx * Ay))
    a = (Px - (b * Bx)) / Ax

    # is the game winnable? if values are integers then yes, otherwise no
    # no partial button presses
    winnable = (a == int(a)) and (b == int(b))

    if winnable:
        cost = (a * cost_A) + (b * cost_B)
        total_cost += cost

print(total_cost)
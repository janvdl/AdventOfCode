import os
from itertools import combinations
from treelib import Tree

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# function to update switches status
def update_switches(state, buttons):
    tmp = state[:]
    for b in buttons:
        tmp[b] *= -1

    return tmp

# tree creation
def build_and_solve(problem) -> int:
    solved = False
    tree = Tree()
    desired_state = [-1 if c == "." else 1 for c in problem[0]]
    start_state = [-1 for c in problem[0]]
    joltage = [int(c) for c in problem[-1].split(",")]
    button_presses = [[int(c) for c in button_press.split(",")] for button_press in problem[1:-1]]
    
    # store the state in data[0]
    # and the button presses in data[1]
    # this helps keep the tree smaller so we don't keep pressing the same buttons
    tree.create_node("Root" + str(start_state), "root", data=[start_state, None])
    n = tree.root

    while not solved:
        leaves = tree.leaves()
        for leaf in leaves:
            for button_press in button_presses:
                if button_press == leaf.data[1]:
                    # dont keep pressing the same buttons
                    continue
                new_state = update_switches(leaf.data[0], button_press)
                tree.create_node(str(button_press) + " : " + str(new_state), None, leaf, data=[new_state, button_press])
                if new_state == desired_state:
                    solved = True
                    print("Solution at ", tree.depth())
                    return tree.depth()
        #clear()
        #tree.show()
        #input()

    return 999

# read input and process
presses = 0
lines = []
for l in open('2025/10/input.txt', 'r').readlines():
    tmp = l.split()
    # remove unnecessary brackets and braces
    for t in range(len(tmp)):
        tmp[t] = tmp[t][1:-1]
    
    p = build_and_solve(tmp)
    presses += p

print(f"Fewest buttons presses: {presses}")
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# you could binary tree it
# but I'm into the idea of just
# using dictionaries as adjacency lists
low_adj = {}
high_adj = {}
values = {}

# recursive function to move values around
def add_or_move_values(values, node_id, value):
    # ensure the entry exists
    if node_id not in values:
        values[node_id] = []

    # add value to the dictionary for this node/output
    values[node_id].append(value)

    # if node has 2 values, move the values to low/high adjacency nodes
    if len(values[node_id]) == 2:
        # sort the values, first goes to low node, second goes to high node
        temp = sorted(values[node_id])
        # reset the values in this node
        values[node_id] = []
        
        if temp == [17, 61]:
            # Part A solution
            print('Part A:', node_id)

        # recursively check that the containers we're moving
        # these values to can actually store them, otherwise
        # trigger the same shuffle of values for their sub-nodes
        add_or_move_values(values, low_adj[node_id], temp[0])
        add_or_move_values(values, high_adj[node_id], temp[1])

# read input
lines = [l.strip() for l in open('2016/10/input.txt', 'r').readlines()]

for line in sorted(lines):
    # the reason for sorting the lines is to have
    # all bot relations captured before starting
    # to assign values

    temp = line.split() # regex is probably better, but w/e
    if temp[0] == 'bot':
        # sort out node vs output IDs
        node_id = ''.join([temp[0], temp[1]])
        low_node_id = ''.join([temp[5], temp[6]])
        high_node_id = ''.join([temp[10], temp[11]])

        # map adjacency list
        low_adj[node_id] = low_node_id
        high_adj[node_id] = high_node_id
    else:
        # get node id
        node_id = ''.join([temp[4], temp[5]])
        add_or_move_values(values, node_id, int(temp[1]))

# Part B solution
partb = values['output0'][0] * values['output1'][0] * values['output2'][0]
print('Part B:', partb)
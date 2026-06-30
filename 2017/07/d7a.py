import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# create node class
class Node:
    def __init__(self, namestr, value=0, parent=None):
        self.namestr = namestr
        self.value = value
        self.parent = None

    def __eq__(self, value):
        if self is None or value is None:
            return False
        else:
            return self.namestr == value.namestr
    
    def addParent(self, parent):
        self.parent = parent
    
    def getParent(self):
        return self.parent

# read nodes
lines = [l.strip().replace(',', '') for l in open('2017/07/input.txt', 'r').readlines()]
nodes = []

while len(lines) > 0:
    line = lines.pop(0)
    l = line.split()
    namestr = l[0]
    value = int(l[1][1:-1])
    children = l[3:]

    proceed = True
    for child in children:
        if Node(child) not in nodes:
            proceed = False
            break
    
    if proceed:
        n = Node(namestr, value)
        nodes.append(n)

        for child in children:
            for nc in nodes:
                if nc.namestr == child:
                    nc.addParent(n)
    else:
        lines.append(line) # move this line to the end so we can process all leaves first

for n in nodes:
    if n.getParent() == None:
        print(n.namestr)
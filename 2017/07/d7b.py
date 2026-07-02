import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# create node class
class Node:
    def __init__(self, namestr, value=0, parent=None, children=[]):
        self.namestr = namestr
        self.value = value
        self.parent = None
        self.children = []

    def __eq__(self, value):
        if self is None or value is None:
            return False
        else:
            return self.namestr == value.namestr
    
    def addParent(self, parent):
        self.parent = parent

    def addChild(self, childNode):
        if childNode not in self.children:
            self.children.append(childNode)
    
    def getParent(self):
        return self.parent
    
    def getChildren(self):
        return self.children
    
    def getTotalValue(self):
        total = 0

        total += self.value
        for child in self.children:
            total += child.getTotalValue()

        return total

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
                    n.addChild(nc)
    else:
        lines.append(line) # move this line to the end so we can process all leaves first

root = None
for n in nodes:
    if n.getParent() == None:
        root = n
        break

def findUnbalancedNode(root):
    children = root.getChildren()
    values = []
    for child in children:
        values.append(child.getTotalValue())
    
    print(values)
    mode = max(set(values), key=values.count)
    offsets = [v for v in values if v != mode]
    if len(offsets) > 0:
        offset = offsets[0]
        unbalanced = [child for child in children if child.getTotalValue() == offset][0]
        print(unbalanced.namestr, "is unbalanced with total value of children", offset, "against", mode)
        balancedweight = unbalanced.value - (offset - mode)
        print(unbalanced.namestr, "should be weight", balancedweight, "if it is the last unbalanced node")
        findUnbalancedNode(unbalanced)

findUnbalancedNode(root)
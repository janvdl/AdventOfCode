import os
from collections import defaultdict
import d21helpers

# set initial program pattern
pattern = defaultdict(int)
pattern['.#./..#/###'] = 1

# read input
debug = False
rules = None
if debug:
    rules = open('2017/21/input_sample.txt', 'r').readlines()
else:
    rules = open('2017/21/input.txt', 'r').readlines()

# build rules dictionary
rulesdict = d21helpers.buildRules(rules)
for i in range(5):
    pattern = d21helpers.iteratePattern(pattern, rulesdict)
    litblocks = d21helpers.countLitBlocks(pattern)
    print(f"At iteration {i + 1} there are {litblocks} lit blocks")
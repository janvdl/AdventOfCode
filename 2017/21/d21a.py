import os
from collections import defaultdict
import d21helpers

# set initial program pattern
pattern = '.#./..#/###'

# read input
debug = True
rules = None
if debug:
    rules = open('2017/21/input_sample.txt', 'r').readlines()
else:
    rules = open('2017/21/input.txt', 'r').readlines()

bla = d21helpers.calculateSplitCount(pattern)
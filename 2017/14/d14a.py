import os
from collections import defaultdict
from knot_hash import knot_hash_bin

debug = False
if debug:
    key = open('2017/14/input_sample.txt', 'r').readline()
else:
    key = open('2017/14/input.txt', 'r').readline()

# count used squares by running over key-0, key-1, ..., key-127
used_squares = 0
for i in range(0, 128):
    curr_key = key + "-" + str(i)
    b = knot_hash_bin(curr_key) # returns binary string 10100000110000100000000101110000...
    used_squares += sum([int(c) for c in b])

print(used_squares)
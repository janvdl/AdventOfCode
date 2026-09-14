import os
from collections import defaultdict

# init variables
debug = False
jumps = None

# read input
if debug:
    jumps = 3
else:
    jumps = 366

# init buffer and position variables
len_buffer = 1 # try to be smart so that we don't have to keep 50M values
buffer_1 = None
pos = 0

# loop 50M times
for x in range(1, 50_000_001):
    pos += jumps
    pos %= len_buffer # avoids having to do another for loop over existing items, just mod the position variable vs the length of array
    pos += 1 # should be placed AFTER the result of mod operation
    len_buffer += 1 # artificially increase buffer length

    if pos == 1:
        # we are only interested in what happens to buffer[1]
        buffer_1 = x

# find value after 0
# 0 is first in the list, so this should be buffer[1]
print(buffer_1)
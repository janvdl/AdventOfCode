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
buffer = [0]
pos = 0

# loop 2017 times
for x in range(1, 2018):
    pos += jumps
    pos %= len(buffer) # avoids having to do another for loop over existing items, just mod the position variable vs the length of array
    pos += 1 # should be placed AFTER the result of mod operation
    buffer.insert(pos, x)

# find index of 2017
index_2017 = buffer.index(2017)
# find value just after 2017
after_2017 = buffer[index_2017 + 1]
print(after_2017)
from collections import defaultdict
import d16_helpers
from bitarray import bitarray

# read input
debug = False
lines = None
if debug:
    lines = open('2016/16/input_sample.txt', 'r').readlines()
    length = 20
else:
    lines = open('2016/16/input.txt', 'r').readlines()
    length = 35651584

input_ = lines[0].strip()
ba = bitarray(len(input_))

for i, v in enumerate(input_):
    ba[i] = int(v)

a = d16_helpers.generate(ba, length)
checksum = d16_helpers.checksum(a)
print(f"Checksum: {checksum}")
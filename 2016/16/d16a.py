from collections import defaultdict
import d16_helpers

# read input
debug = False
lines = None
if debug:
    lines = open('2016/16/input_sample.txt', 'r').readlines()
    length = 20
else:
    lines = open('2016/16/input.txt', 'r').readlines()
    length = 272

input_ = [int(c) for c in lines[0]]
a = d16_helpers.generate(input_, length)
checksum = d16_helpers.checksum(a)
print(f"Checksum: {checksum}")
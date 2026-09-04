import os
from collections import defaultdict

# load input
debug = False
if debug:
    lines = [l.strip() for l in open('2017/13/input_sample.txt', 'r').readlines()]
else:
    lines = [l.strip() for l in open('2017/13/input.txt', 'r').readlines()]

# initiate firewall
firewall = defaultdict(int)

for line in lines:
    parts = line.split(":")
    layer_, range_ = int(parts[0]), int(parts[1]) - 1 # subtract 1 for 0-indexed ranges (depths) - this works better for the modulo calculation below
    firewall[layer_] = range_

last_scanner_index = max(firewall)

# function to determine where the firewall scanner is based on current picosecond
def scanner_pos(firewall, layer, picosecond) -> int:

    if picosecond != 0:
        range_ = firewall[layer]

        if range_ != 0:
            # 1 is down, -1 is up
            direction = 1 if (picosecond // range_) % 2 == 0 else -1
            offset = picosecond % range_
            pos = offset if direction == 1 else range_ - offset
            return pos
        else:
            # no scanner in this layer
            return -1
    else:
        # at picosecond 0, the scanner is in the 0th row
        return 0

# initial packet_pos is at 0
packet_pos = 0
severity = 0
for picosecond in range(0, last_scanner_index + 1):
    pos = scanner_pos(firewall, packet_pos, picosecond)
    print(f"Scanner in layer {packet_pos} at picosecond {picosecond} is at position {pos}")
    if pos == 0:
        # caught
        severity += packet_pos * (firewall[packet_pos] + 1) # range should be 1-indexed for the severity count
    packet_pos += 1

print(f"Severity = {severity}")
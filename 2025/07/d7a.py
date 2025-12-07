import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2025/07/input.txt', 'r').readlines()]

# find location of S
s_r, s_c = 0, lines[0].find("S")

# keep track of beams and splits
splits = 0
beam_cols = defaultdict(int)
beam_cols[s_c] = 1

for l in lines[1:]:
    split_idxs = [x for x, c in enumerate(l) if c == "^"]

    tmp_beam_cols = beam_cols.copy()
    for b in tmp_beam_cols:
        if b in split_idxs and beam_cols[b] > 0:
            splits += 1
            beam_cols[b - 1] = 1
            beam_cols[b + 1] = 1
            beam_cols[b] = 0

print(splits)
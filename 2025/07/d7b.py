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

            # every beam arrives in its path based on the previous splitter
            # like a sort of Pascal's triangle
            # in the case of a split setup like:
            #       S
            #       |        <- one timeline
            #       ^        
            #     |   |      <- inherits one timelines each from above
            #     ^   ^
            #   |   |   |    <- left and right beams inherit one timeline, middle beam has 2 timelines
            # 
            #   in the bottom row, the total timelines are 1 + 2 + 1 = 4
            #   only need to add up the possibilities of the last row since 
            #   they contain all prev. timelines already
            beam_cols[b - 1] += beam_cols[b]
            beam_cols[b + 1] += beam_cols[b]
            beam_cols[b] = 0

timelines = 0
for b in beam_cols:
    timelines += beam_cols[b]
print(timelines)
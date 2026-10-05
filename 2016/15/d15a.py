from collections import defaultdict
from d15_helpers import Disc

# dictionary for discs
discs = {}

# read input
debug = False
lines = None
if debug:
    discs[0] = Disc(numpos=5, startpos=4)
    discs[1] = Disc(numpos=2, startpos=1)
else:
    discs[0] = Disc(numpos=17, startpos=1)
    discs[1] = Disc(numpos=7, startpos=0)
    discs[2] = Disc(numpos=19, startpos=2)
    discs[3] = Disc(numpos=5, startpos=0)
    discs[4] = Disc(numpos=3, startpos=0)
    discs[5] = Disc(numpos=13, startpos=5)

# check positions
done = False
time = 0
prevtime = None # to keep track of the time at which the while was entered - this is advanced by 1 each run
while not done:
    prevtime = time
    for k, disc in discs.items():
        time += 1
        if disc.pos_at_time(time) == 0:
            if k == len(discs) - 1:
                print(f"Hit the button at time {prevtime} for the capsule to fall through")
                done = True
                break
        else:
            # reset to 1 sec after the current start
            time = prevtime + 1
            break
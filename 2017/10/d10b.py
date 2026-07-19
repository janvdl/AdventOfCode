import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

debug = False
if debug:
    lst = [i for i in range(0, 5)]
    lengths_tmp = "1,2,3"
else:
    lst = [i for i in range(0, 256)]
    lengths_tmp = open('2017/10/input.txt', 'r').readline()

# convert each char to ascii equivalent
lengths = []
for c in lengths_tmp:
    lengths.append(ord(c))

# add pre-specified lengths in problem statement
lengths += [17, 31, 73, 47, 23]

cursor_idx = 0
skip = 0
max_idx = len(lst)

# run for 64 iterations
for runno in range(0, 64):
    print("Starting run", runno)
    for length in lengths:
        if length > max_idx:
            # invalid instruction, ignore and move on
            print("length specified is too long for the list")
            continue
        elif length == 0 or length == 1:
            # nothing to do, just move the cursor and increase the skip
            cursor_idx += length + skip
            cursor_idx %= max_idx

            skip += 1 # finally, increase skip length
            continue

        # find the start and end indices, handle possible wrap arounds
        sublst_start = cursor_idx
        sublst_end = sublst_start + length
        sublst_end %= max_idx

        if sublst_start < sublst_end:
            # we're gucci like vespucci
            sublst = lst[sublst_start:sublst_end]
            sublst.reverse()
            lst[sublst_start:sublst_end] = sublst[:]
        else:
            # need to wrap around; split the list into two blocks, fuse, reverse, and put back
            sublst1 = lst[sublst_start:max_idx]
            sublst2 = lst[0:sublst_end%max_idx]
            sublst = sublst1 + sublst2
            sublst.reverse()
            lst[sublst_start:max_idx] = sublst[0:len(sublst1)]
            lst[0:sublst_end%max_idx] = sublst[len(sublst1):]

        cursor_idx += length + skip
        cursor_idx %= max_idx

        skip += 1 # finally, increase skip length

# calculate "dense hash" in chunks of 16 values
dense_hash = []
while len(lst) > 0:
    chunk = lst[0:16]
    hash_tmp = chunk[0]
    for x in chunk[1:]:
        hash_tmp ^= x
    dense_hash.append(hex(hash_tmp)[2:]) # hex equivalent, remove 0x prefix

    lst = lst[16:]
    print(chunk)

final_hash = ''.join(dense_hash)
print(final_hash, "length =", len(final_hash))
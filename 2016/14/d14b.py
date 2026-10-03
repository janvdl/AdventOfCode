from collections import defaultdict
import d14_helpers

# read input
debug = False
lines = None
if debug:
    lines = open('2016/14/input_sample.txt', 'r').readlines()
else:
    lines = open('2016/14/input.txt', 'r').readlines()

# hash dictionaries
hashes = defaultdict(str) # this dictionary stores all hashes to try and find valid 5-repeats first
keyhashes = "" # this string will store the keychars to generate a 64-length string of keychars

prefix = lines[0]
done = False
cursor = 0

while not done:
    # create hash at cursor index if it does not exist
    if cursor not in hashes:
        d14_helpers.generate_next_hash(hashes, prefix, cursor, partB=True)

    # check for a 3-repeat
    rep3, key3 = d14_helpers.repeat3(hashes[cursor])

    if not rep3:
        cursor += 1 # continue if no 3-repeat found
    else:
        # a 3-repeat was found, generate the next 1000 hashes
        d14_helpers.generate_next_hash(hashes, prefix, cursor + 1, 1000, partB=True)
        
        # check that the next 1000 hashes has a 5-repeat with the same key as the 3-repeat
        for k in range(cursor + 1, cursor + 1001):
            if key3 * 5 in hashes[k]:
                # store this key in the keyhashes string until we get 64 of them
                keyhashes += key3
                print(f"{cursor} :: {hashes[cursor]} --- 5: {k} :: {hashes[k]} --- key = {key3}")

                if len(keyhashes) == 64:
                    print(f"At cursor {cursor}, the 64th key was found, rendering the following len64 keystring {keyhashes}")
                    done = True

                break

        # continue the search
        cursor += 1

#print(hashes)
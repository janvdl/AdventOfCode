hex2bin = {}
hex2bin['0'] = '0000'
hex2bin['1'] = '0001'
hex2bin['2'] = '0010'
hex2bin['3'] = '0011'
hex2bin['4'] = '0100'
hex2bin['5'] = '0101'
hex2bin['6'] = '0110'
hex2bin['7'] = '0111'
hex2bin['8'] = '1000'
hex2bin['9'] = '1001'
hex2bin['a'] = '1010'
hex2bin['b'] = '1011'
hex2bin['c'] = '1100'
hex2bin['d'] = '1101'
hex2bin['e'] = '1110'
hex2bin['f'] = '1111'

def knot_hash_hex(s):
    lst = [i for i in range(0, 256)]

    # convert each char to ascii equivalent
    lengths = []
    for c in s:
        lengths.append(ord(c))

    # add pre-specified lengths in problem statement
    lengths += [17, 31, 73, 47, 23]

    cursor_idx = 0
    skip = 0
    max_idx = len(lst)

    # run for 64 iterations
    for runno in range(0, 64):
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

        hex_tmp = hex(hash_tmp)[2:]
        if len(hex_tmp) < 2:
            hex_tmp = "0" + hex_tmp # this was an unhandled case in my D10 solution
        dense_hash.append(hex_tmp) # hex equivalent, remove 0x prefix

        lst = lst[16:]

    hex_hash = ''.join(dense_hash)
    return hex_hash

def knot_hash_bin(s):
    hex_hash = knot_hash_hex(s)

    bin_hash = ''
    for h in hex_hash:
        bin_hash += hex2bin[h] # binary equivalent of each hex char is appended to bin_hash
    return bin_hash
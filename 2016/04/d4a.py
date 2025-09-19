import os
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/04/input.txt', 'r').readlines()]

# process lines
real_room_count = 0

for line in lines:
    line_split = line.split('[')
    
    # get the 3 components of each room code separately
    encrypted_name = ''.join([c for c in line_split[0] if c.isalpha()])
    sector_id = int(''.join([n for n in line_split[0] if n.isdigit()]))
    checksum = ''.join([c for c in line_split[1] if c.isalpha()])
    print(encrypted_name, ':', sector_id, ':', checksum)

    # keep a dict of all char counts in the encrypted name
    # then select the top 5 counts and the characters associated with them
    cc = defaultdict(int)
    for c in encrypted_name:
        cc[c] += 1

    counts = []
    for k,v in cc.items():
        counts.append(v)

    # make sure we have no invalid chars in the checksum, i.e., must be in the top 5 of counts
    allowed_checksum_chars = [k for k,v in cc.items() if v in sorted(counts, reverse=True)[:5]]
    invalid_checksum_chars = [x for x in checksum if x not in allowed_checksum_chars]

    if len(invalid_checksum_chars) == 0:
        # loop over each char (except last) in the checksum and ensure that the
        # count of each is greater or equal than the next
        for x in range(len(checksum) - 1):
            c1 = encrypted_name.count(checksum[x])
            c2 = encrypted_name.count(checksum[x + 1])
            print('Comparing', checksum[x], ':', c1, 'versus', checksum[x + 1], ':', c2)
            if c1 < c2:
                print('Breaking - this is a decoy room (smaller)')
                break
            elif encrypted_name.count(checksum[x]) == encrypted_name.count(checksum[x + 1]):
                if checksum[x] > checksum[x + 1]:
                    print('Breaking - this is a decoy room (equal, but non-alphabetical)')
                    break
        else:
            print('This is a real room, adding', sector_id, 'to count')
            real_room_count += sector_id
        
        print("====================================")

print(real_room_count)
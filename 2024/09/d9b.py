import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# import data
data  = open('input_a.txt', 'r').read().strip()
disk = {} # capture the item and its length to shift only whole blocks

# expand both the disk entries and the free space
fileindex = 0
for idx, item in enumerate(data):
    fileindex = int(idx / 2)
    disk[idx] = []
    if idx % 2 == 0:
        for _ in range(int(item)):
            disk[idx].append(str(fileindex))
    else:
        for _ in range(int(item)):
            disk[idx].append('.')

# compress the data by moving blocks of .'s to the end and moving data from the end into their place
l = len(disk)
j = l - 1
for k in range(j, 0, -1):
    blocksize = len(disk[k])
    blockfree = disk[k].count('.')
    if blocksize == blockfree:
        continue
    if blocksize > 0:
        for i in range(0, j):
            if i < k:
                blockfree = disk[i].count('.')
                if blocksize <= blockfree:
                    print('Block', i, 'has free space of size', blockfree, 'to fit block', k, disk[k])
                    for x in range(0, blocksize):
                        offset = disk[i].index('.')
                        disk[i].pop()
                        disk[i].insert(offset, disk[k][x])
                        disk[k][x] = '.'
                    break
            else:
                break

# calculate checksum
checksum = 0
counter = -1
for i in range(len(disk)):
    for j in range(len(disk[i])):
        counter += 1
        if disk[i][j] == ".":
            continue
        checksum += (counter * int(disk[i][j]))

print(checksum)
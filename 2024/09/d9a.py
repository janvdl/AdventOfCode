import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# import data
data  = open('input_a.txt', 'r').read().strip()
disk = []

# expand both the disk entries and the free space
for idx, item in enumerate(data):
    for _ in range(int(item)):
        if idx % 2 == 0:
            fileindex = int(idx /2)
            disk.append(str(fileindex))
        else:
            disk.append('.')

# compress the data by moving .'s to the end and moving data from the end into their place
l = len(disk)
i = 0
j = l - 1
while i < j:
    if disk[i] != '.':
        i += 1
        continue

    if disk[j] == '.':
        j -= 1
        continue

    disk[i] = disk[j]
    disk[j] = '.'

# calculate checksum
checksum = 0
for i in range(len(disk)):
    if disk[i] == ".":
        continue
    checksum += (i * int(disk[i]))

print(checksum)
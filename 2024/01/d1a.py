import re

# initialise arrays to keep track of the numbers
left_array = []
right_array = []

with open('input_a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # regex to extract the left/right numbers
        numbers = re.findall(r'\d+', line)
        left_array.append(int(numbers[0]))
        right_array.append(int(numbers[1]))

# sort the left/right arrays
left_array.sort()
right_array.sort()

# add up the distances between elements et voila
total_distance = 0
for i in range(len(left_array)):
    # bear in mind that distance is an absolute value
    total_distance += abs(left_array[i] - right_array[i])

print(total_distance)

import re

# initialise dictionaries for keeping track of the numbers
left_instances = {}
right_instances = {}

with open('input_b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # regex to extract the left/right numbers
        numbers = re.findall(r'\d+', line)
        left_num = int(numbers[0])
        right_num = int(numbers[1])

        # keep track of the counts of each number in the left column
        if left_num not in left_instances:
            left_instances[left_num] = 1
        else:
            left_instances[left_num] += 1

        # defensive programming; if a number in the left column does not appear in the right,
        # then initialise with a zero count, otherwise the bit where we multiply with right_instances[n]
        # below will error
        if left_num not in right_instances:
            right_instances[left_num] = 0

        #keep track of the counts of each number in the right column
        if right_num not in right_instances:
            right_instances[right_num] = 1
        else:
            right_instances[right_num] += 1

# multiply and add up the similarity scores
similarity_score = 0
for n in left_instances:
    temp_score = n * left_instances[n] * right_instances[n]
    similarity_score += temp_score

print(similarity_score)

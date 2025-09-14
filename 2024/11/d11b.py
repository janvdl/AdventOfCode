import os
import functools

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# dict to store counts instead of actual nums
nums = {}

# import data
data = open('input_a.txt', 'r').read().split()
for num in data:
    nums[num] = 1 # initialise each with a count of 1

# define the "blink" function
# i had to look this up because my solution in Part A would have run for probably an hour
# essentially, by using a dictionary, we just keep track of the counts of elements,
# instead of all the elements themselves
def blink(nums):
    temp_nums = {}
    temp_nums['1'] = 0 # easy to initialise

    for num in nums:
        if num == '0':
            temp_nums['1'] += nums['0']
        elif len(num) % 2 == 0:
            middle = int(len(num) / 2)
            firsthalf = str(int(num[:middle]))
            secondhalf = str(int(num[middle:]))

            # init
            if firsthalf not in temp_nums:
                temp_nums[firsthalf] = 0
            if secondhalf not in temp_nums:
                temp_nums[secondhalf] = 0

            temp_nums[firsthalf] += nums[num]
            temp_nums[secondhalf] += nums[num]
        else:
            temp_num = str(int(num) * 2024)
            if temp_num not in temp_nums:
                temp_nums[temp_num] = 0
            temp_nums[temp_num] += nums[num]
    return temp_nums

# do the blinks
num_of_blinks = 75
for i in range(num_of_blinks):
    print("Processing blink", i + 1)
    nums = blink(nums)

# add up all the elements
total = 0
for x in nums:
    total += nums[x]
print(total)
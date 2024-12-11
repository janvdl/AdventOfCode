import os
import functools

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# import data
nums  = open('input_a.txt', 'r').read().split()
print(nums)

# define the "blink" function
def blink(nums):
    temp_nums = []
    while (len(nums) > 0):
        num = nums.pop(0)
        if num == '0': # zeroes become ones
            num = '1'
            temp_nums.append(num)
        elif len(num) % 2 == 0: # even number of digits get split
            middle = int(len(num) / 2)
            firsthalf = str(int(num[:middle])) 
            secondhalf = str(int(num[middle:])) # so that 000 becomes 0, for example
            temp_nums.append(firsthalf)
            temp_nums.append(secondhalf)
        else: # otherwise multiply by 2024
            num = str(int(num) * 2024)
            temp_nums.append(num)

    return temp_nums

num_of_blinks = 25
for i in range(num_of_blinks):
    #print("Now processing blink", i + 1)
    nums = blink(nums)
    print("After", i + 1, "blinks you have", len(nums), "stones")
    #print(nums)
import re
import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# all calibration lines
cal_lines = []

# read and parse input
with open('input_a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # regex to extract the mul() statement
        num_matches = re.findall(r'\d+', line)
        cal_line = []
        for num in num_matches:
            cal_line.append(int(num))
        cal_lines.append(cal_line)

# try all combinations of + and *, eval from left to right, no op precedence
def recurseOp(ans, currval, nums):
    if currval > ans:
        return False
    elif len(nums) > 0:
        num = nums.pop()
        addition = currval + num
        multiplication = currval * num
        #print("ans = ", ans, ", currval = ", currval, ", num = ", num, ", addition = ", addition, ", multiplication = ", multiplication, ", nums = ", nums)

        if len(nums) == 0 and (ans == addition or ans == multiplication):
            return True
        else:
            return recurseOp(ans, addition, nums.copy()) or recurseOp(ans, multiplication, nums.copy())
    else:
        return False

# shove each calibration line into recurseOp() 
def solve(cal_line):
    ans = cal_line[0]
    first_num = cal_line[1]
    nums = cal_line[2:]
    nums.reverse()
    
    ansIsPossible = recurseOp(ans, first_num, nums)
    return ansIsPossible

# add up all the lines that can be solved with the operators provided
total = 0
for cal_line in cal_lines:
    if solve(cal_line):
        total += cal_line[0]
print("Total = ", total)
import copy
safeLines = 0

def checkNumberOfDups(lst):
    # check number of duplicates (use original array)
    numOfDups = len(lst) - len(set(lst))
    return numOfDups

def checkNumberOfChanges(lst):
    # check for change of sign (these are non-monotonous changes) (use diff array)
    numOfNeg = sum(1 for x in lst if x < 0)
    numOfPos = sum(1 for x in lst if x > 0)
    numOfChanges = min(numOfNeg, numOfPos)
    return numOfChanges

def checkNumberOfGE3(lst):
    # check for diffs greater than 3
    numOfGE3 = sum(1 for x in lst if abs(x) > 3)
    return numOfGE3

def isSafe(original_lst, diff_lst):
    # total number of problems
    numOfProbs = checkNumberOfDups(original_lst) + checkNumberOfChanges(diff_lst) + checkNumberOfGE3(diff_lst)
    return numOfProbs <= 0

# open input file and start processing
with open('input_sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        temp = list(map(int, line.split()))

        tempdiff = []
        for x,y in zip(temp, temp[1:]):
            diff = (x - y)
            tempdiff.append(diff)

        if isSafe(temp, tempdiff):
            safeLines += 1

print(safeLines)

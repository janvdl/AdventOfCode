safeLines = 0

# check whether list is monotonously increasing
def isSafe(lst):
    # check for dups, easy false
    if len(lst) != len(list(set(lst))):
        return False

    # check whether it's equal to its sorted self, else easy false
    if lst != sorted(lst):
        return False

    # check for any increases greater than 3
    if increaseMoreThan3(lst):
        return False

    # if none of the above are triggered, we're safe
    return True

# check if the list is increasing, else we can reverse it
def isIncreasing(lst):
    return lst[0] < lst[-1]

# increases > 3 are not allowed
def increaseMoreThan3(lst):
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] > 3:
            return True
    return False

# open input file and start processing
with open('input_a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        temp = list(map(int, line.split()))

        # if not increasing, just reverse it, as long as it's monotonous
        if not isIncreasing(temp):
            temp.reverse()

        if isSafe(temp):
            safeLines += 1

print(safeLines)

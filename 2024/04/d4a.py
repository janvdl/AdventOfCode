total = 0
xmas_array = []

def checkForXmas(s):
    global total
    count = (s.count("XMAS") + s.count("SAMX"))
    if count > 0:
        total += count

# read input data and create array of chars
with open('input_bigboy.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        xmas_array.append(list(line.replace("\n", "")))

# loop through input
rows = len(xmas_array)
cols = len(xmas_array[0])

horizontal_stack = []
vertical_stack = []
diagonal_stack1 = [] # need one running top left to bottom right
diagonal_stack2 = [] # need one running top right to bottom left

for i in range(rows):
    horizontal_stack.clear()
    vertical_stack.clear()

    # create horizontal and vertical stacks
    for j in range(cols):
        diagonal_stack1.clear()
        diagonal_stack2.clear()
        horizontal_stack.append(xmas_array[i][j])
        vertical_stack.append(xmas_array[j][i])

        # build diagonals
        if i == 0 or j == 0:
            for k in range(min(cols - j, rows - i)):
                diagonal_stack1.append(xmas_array[i + k][j + k])
                diagonal_stack2.append(xmas_array[i + k][cols - (j + k + 1)])
            d1 = ''.join(diagonal_stack1)
            checkForXmas(d1)
            d2 = ''.join(diagonal_stack2)
            checkForXmas(d2)

    h = ''.join(horizontal_stack)
    checkForXmas(h)
    v = ''.join(vertical_stack)
    checkForXmas(v)

print("XMAS count: ", total)
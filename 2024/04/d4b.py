total = 0
xmas_array = []

with open('input_bigboy.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        xmas_array.append(list(line.replace("\n", "")))

# loop through input
rows = len(xmas_array)
cols = len(xmas_array[0])

for i in range(rows - 2):
    for j in range(cols - 2):
        if xmas_array[i + 1][j + 1] == "A":
            # proceed if there is an A in the middle
            tlbr = ''.join(sorted(xmas_array[i][j] + xmas_array[i + 2][j + 2])) # top left to bottom right
            trbl = ''.join(sorted(xmas_array[i][j + 2] + xmas_array[i + 2][j])) # top right to bottom left

            if tlbr == "MS" and trbl == "MS":
                # X-MAS exists
                total += 1

print(total)
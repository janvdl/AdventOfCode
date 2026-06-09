# It makes more sense to solve this one by hand, I think.

# ===

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

# Notice that on the right diagonal going down, it follows a pattern of odd numbers squared
# i.e., 1^2, 3^2, 5^2

# Hence, for input << 277678 >> take sqrt of the input to figure out where it sits.
# sqrt(277678) = 526.95 approx, i.e., must be somewhere between 525^2 and 527^2

# if you were dealing with square of size 3^2,  the min dist = 1 and the max dist = 2
# if you were dealing with square of size 5^2,  the min dist = 2 and the max dist = 4
# if you were dealing with square of size 7^2,  the min dist = 3 and the max dist = 6
# if you were dealing with square of size 9^2,  the min dist = 4 and the max dist = 8
# if you were dealing with square of size 11^2, the min dist = 5 and the max dist = 10
# if you were dealing with square of size 13^2, the min dist = 6 and the max dist = 12
# if you were dealing with square of size 15^2, the min dist = 7 and the max dist = 14
# if you were dealing with square of size 17^2, the min dist = 8 and the max dist = 16
# if you were dealing with square of size 19^2, the min dist = 9 and the max dist = 18
# etc.
# if you were dealing with square of size n^2,  the min dist = (n - 1) / 2 and the max dist = (n - 1)

# Thus, for input 277678 (square of n = 527^2) the answer must be somewhere between 263 and 526

# ===

# bottom right corner value = 527^2 = 277729
# bottom left corner value = bottom right corner value - (527 - 1) = 277203
# the distance to the exact midpoint between these 2 corner values is the shortest, i.e., 263
# the exact midpoint between these 2 corners is: 277466
# so you need d1 = 263 to get to the midpoint
# and then d2 = (277678 - 277466) = 212 to move sideways (Manhattan geometry)

# ===

# d = d1 + d2 = 263 + 212 = 475
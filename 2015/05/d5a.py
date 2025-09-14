from collections import defaultdict
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# dictionary for character counts
char_count = defaultdict(int)

# read input
lines = [line.strip() for line in open('2015/05/input_a.txt', 'r')]

# check which strings are naughty or nice
# make a list and check it twice
nice_count = 0
for line in lines:
    char_count.clear()
    i = 0
    while i <= len(line) - 2:
        substr = line[i : i + 2]   # grab each pair of characters, shifting by 1 each time
        char_count[substr] += 1    # increment each pair of characters
        char_count[substr[0]] += 1 # increment first character of each pair (otherwise we'll double count)
        i += 1
    char_count[line[-1]] += 1      # increment last character (this won't be grabbed in the code above)
    
    vowels = sum([char_count[v] for v in char_count.keys() if v in 'aeiou']) # sum the vowels
    double = sum([1 for d in char_count.keys() if len(d) == 2 and d[0] == d[1]]) # check if there are any pairs that are the same letter
    bad    = sum([1 for b in char_count.keys() if b in ['ab', 'cd', 'pq', 'xy']]) # check for any bad strings

    if vowels >= 3 and double >= 1 and bad == 0:
        nice_count += 1

print(nice_count)
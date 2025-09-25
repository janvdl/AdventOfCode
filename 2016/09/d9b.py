import os
import re
from collections import defaultdict

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
line = open('2016/09/input.txt', 'r').readline().strip()

# dictionary for character count
cc = defaultdict(int)

# recursive function to decompress and count all chars
def solve(s, cc, multi):
    '''
    s: string to decompress
    cc: char count dictionary reference
    multi: multiplier for the character
    '''
    if len(s) == 0:
        # terminal case
        return
    elif len(s) == 1:
        # pre-terminal case
        temp, s = s[0], ''
    else:
        # investigate first char, split from rest of string
        temp, s = s[0], s[1:]

    if temp.isalpha():
        # if the first char is an alpha string
        # add the multiplier to the count for this character
        cc[temp] += multi
        # solve the remainder of the string
        solve(s, cc, multi)
    elif temp == '(':
        # otherwise, if it's an open paren
        # keep popping until close paren
        while temp[-1] != ')':
            temp += s[0]
            s = s[1:]
        else:
            # after close paren, extract len x rep info
            numbers = re.findall('\d+', temp)
            marker_len = int(numbers[0])
            marker_rep = int(numbers[1])

            # split between the marked length and rest
            sub = s[0:marker_len]
            rest = s[marker_len:]

            # the marked length string needs to take the
            # rep multiplier into account to add into the dict
            solve(sub, cc, multi * marker_rep)

            # solve the rest (adjacent to sub), with existing multi
            solve(rest, cc, multi)

# call the recursive func
solve(line, cc, multi = 1)

# add up all the chars
total = 0
for k,v in cc.items():
    print(k, ':', v)
    total += v
print(total)
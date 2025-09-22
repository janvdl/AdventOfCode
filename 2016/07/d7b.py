import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/07/input.txt', 'r').readlines()]

# function to look for pairs
# for an extra challenge, skipping regex
def check_ssl(input):
    supports_ssl = False
    in_brackets = False

    outers = []
    inners = []

    for i in range(len(input) - 2):
        sub = input[i : i + 3]
        if '[' in sub:
            in_brackets = True
            continue
        elif ']' in sub:
            in_brackets = False
            continue
        else:
            # check for xyyx / abba pattern
            if sub[0] == sub[2] and sub[0] != sub[1]:
                if in_brackets:
                    inners.append(sub)
                    continue
                else:
                    outers.append(sub)
                    continue
    
    # check if adding up the ordinals of the characters leads to 3 of the same
    for i in inners:
        for o in outers:
            i_ord = [ord(c) for c in i]
            o_ord = [ord(c) for c in o]
            
            # make sure they are each others inverse, i.e., xyx and yxy
            if i_ord[0] == o_ord[1] and i_ord[1] == o_ord[0]:
                supports_ssl = True
                break
        
        if supports_ssl:
            break # no need to keep looping if we have ssl support

    return supports_ssl

# process lines
valid_ssl = 0
for line in lines:
    valid_ssl += 1 if check_ssl(line) else 0

# final count
print('SSL supporting addresses:', valid_ssl)
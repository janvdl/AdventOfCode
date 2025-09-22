import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# read input
lines = [l.strip() for l in open('2016/07/input.txt', 'r').readlines()]

# function to look for pairs
# for an extra challenge, skipping regex
def check_tls(input):
    supports_tls = False
    in_brackets = False

    for i in range(len(input) - 3):
        sub = input[i : i + 4]
        if '[' in sub:
            in_brackets = True
            continue
        elif ']' in sub:
            in_brackets = False
            continue
        else:
            # check for xyyx / abba pattern
            if sub[0] == sub[3] and sub[1] == sub[2] and sub[0] != sub[1]:
                if in_brackets:
                    supports_tls = False
                    break
                else:
                    supports_tls = True
                    continue

    return supports_tls

# process lines
valid_tls = 0
for line in lines:
    valid_tls += 1 if check_tls(line) else 0

# final count
print('TLS supporting addresses:', valid_tls)
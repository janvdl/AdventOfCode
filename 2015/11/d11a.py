import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define input_
input_ = 'hxbxwxba'

def increment_pass(s):
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        if s[i] == 'z':
            s[i] = 'a'
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    return ''.join(s)

def is_valid(s):
    if 'i' in s or 'o' in s or 'l' in s: # check for invalid characters
        return False
    
    if not any([ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) + 1 == ord(s[i+2]) for i in range(len(s) - 2)]): # check for straight increment, e.g., abc, bcd, etc.
        return False
    
    # check for 2 pairs of different characters
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            for j in range(i+2, len(s) - 1):
                if s[j] == s[j+1] and s[j] != s[i]:
                    return True
    return False

while not is_valid(input_):
    input_ = increment_pass(input_)
print(input_)
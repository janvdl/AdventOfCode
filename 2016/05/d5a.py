import os
import hashlib

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def my_md5(input):
    return hashlib.md5(input.encode()).hexdigest()

# define input string and password placeholder
input = 'uqwqemis'
password = ''

# brute force
i = 0
while len(password) < 8:
    i += 1
    md5 = my_md5(input + str(i))
    if md5.startswith('00000'):
        print(i)
        password += md5[5]

# print final result
print('Password:', password)
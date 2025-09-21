import os
import hashlib
import random

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


def my_md5(input):
    return hashlib.md5(input.encode()).hexdigest()

# define input string and password placeholder
input = 'uqwqemis'
password = {}

for i in range(8):
    password[i] = '_'

# brute force
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
i = 0
while '_' in password.values():
    i += 1
    md5 = my_md5(input + str(i))
    if md5.startswith('00000'):
        index = md5[5]
        if str(index).isdigit() and int(index) in password:
            password[int(index)] = md5[6] if password[int(index)] == '_' else password[int(index)]

        # cool hacker effect
        for j in range(8):
            print(random.choice(characters) if password[j] == '_' else password[j], end='')
        print('\r', end='')

# print final result
for j in range(8):
    print(password[j], end='')
print('\nDone')
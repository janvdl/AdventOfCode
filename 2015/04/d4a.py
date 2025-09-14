import hashlib
import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define input
prefix = 'bgvyzdsv'
for i in range(1000000):
    if (hashlib.md5((prefix + str(i)).encode())).hexdigest().startswith('00000'):
        print(i)
        break
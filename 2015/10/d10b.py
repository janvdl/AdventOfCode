import os
import math

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define input_
input_ = '3113322113'

def look_and_say(input_):
    output_ = ''

    counts = {}

    for i in range(len(input_) + 1):
        if i == len(input_):
            output_ += str(counts[input_[i-1]]) + input_[i-1]
            counts.clear()
            return output_

        if i >= 1 and input_[i] != input_[i-1]:
            output_ += str(counts[input_[i-1]]) + input_[i-1]
            counts.clear()

        if input_[i] in counts:
            counts[input_[i]] += 1
        else:
            counts[input_[i]] = 1

for i in range(50):
    input_ = look_and_say(input_)
    print(i, len(input_))
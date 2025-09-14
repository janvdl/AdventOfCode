import os

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define input_
input_ = '3113322113'

def look_see(input_):
    output_ = ''
    count = 0
    last_char = ''

    input_ = list(input_)
    while len(input_) > 0:
        char = input_.pop(0)

        if last_char == '':
            last_char = char
            count = 1
        elif last_char == char:
            count += 1
        else:
            output_ += str(count) + last_char
            last_char = char
            count = 1
    
    # flush the last character into output_
    output_ += str(count) + last_char
    
    return output_

for i in range(40):
    output_ = look_see(input_)
    input_ = output_
    print(i, len(output_))
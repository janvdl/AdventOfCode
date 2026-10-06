def step(a: str) -> str:
    b = a[::-1]
    b = ''.join(['1' if c == '0' else '0' for c in b])
    return (a + '0' + b)

assert(step('1') == '100')
assert(step('0') == '001')
assert(step('11111') == '11111000000')
assert(step('111100001010') == '1111000010100101011110000')

def generate(input_, length):
    a = input_

    # keep expanding until we are at or over the length required
    while len(a) < length:
        a = step(a)

    a = a[:length]

    return a

assert(generate('10000', 20) == '10000011110010000111')

def checksum(s: str) -> str:
    if len(s) % 2 != 0:
        return s
    else:
        split = [(s[i:i+2]) for i in range(0, len(s), 2)]
        s_new = ''.join(['1' if s_[0] == s_[1] else '0' for s_ in split])
        return checksum(s_new)

assert(checksum('110010110100') == '100')
assert(checksum('10000011110010000111') == '01100')
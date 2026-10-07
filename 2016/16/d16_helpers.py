def step(a: list[int]) -> list[int]:
    b = a[::-1]
    b = [1 if x == 0 else 0 for x in b]
    return (a + [0] + b)

assert(step([1]) == [1, 0, 0])
assert(step([0]) == [0, 0, 1])

def generate(input_, length):
    a = input_

    # keep expanding until we are at or over the length required
    while len(a) < length:
        a = step(a)

    a = a[:length]

    return a

assert(generate([1, 0, 0, 0, 0], 20) == [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1])

def checksum(a: list[int]) -> str:
    if len(a) % 2 != 0:
        return ''.join([str(x) for x in a])
    else:
        a_new = []
        for i in range(0, len(a), 2):
            a1 = a.pop(0)
            a2 = a.pop(0)
            a_new.append(1 if a1 == a2 else 0)
        return checksum(a_new)

assert(checksum([1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == '100')
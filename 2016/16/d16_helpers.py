from bitarray import bitarray

def step(a: bitarray) -> bitarray:
    b = ~a[::-1]
    return (a + bitarray('0') + b)

assert(step(bitarray('1')) == bitarray('100'))
assert(step(bitarray('0')) == bitarray('001'))

def generate(ba: bitarray, length: int) -> bitarray:
    a = ba

    # keep expanding until we are at or over the length required
    while len(a) < length:
        done_perc = int((len(a) / length) * 100)
        print(f"Expansion: {done_perc}%")
        a = step(a)

    a = a[:length]
    print("Done with expansion")

    return a

assert(generate(bitarray('10000'), 20) == bitarray('10000011110010000111'))

def checksum(a: bitarray) -> bitarray:
    print(f"Checksum in progress :: input length is {len(a)}")
    if len(a) % 2 != 0:
        return a
    else:
        a_new = bitarray(len(a) // 2)
        for i in range(0, len(a), 2):
            a_new[i // 2] = a[i] == a[i + 1]
        return checksum(a_new)

assert(checksum(bitarray('110010110100')) == bitarray('100'))
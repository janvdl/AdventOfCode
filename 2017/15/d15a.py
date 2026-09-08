import os
from collections import defaultdict

# initialise generator dictionary, multiplier values, and mod value
gen = defaultdict(int)

multiplier = {
    'A': 16807,
    'B': 48271
}

mod = 2147483647

# read input
debug = False
lines = None
if debug:
    lines = open('2017/15/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/15/input.txt', 'r').readlines()

gen['A'] = int(lines[0].split()[-1])
gen['B'] = int(lines[1].split()[-1])

# run loop
judge_total = 0
total_runs = 40_000_000
for x in range(total_runs):
    gen['A'] = (gen['A'] * multiplier['A']) % mod
    gen['B'] = (gen['B'] * multiplier['B']) % mod

    bin_a = bin(gen['A'])[2:][-16:] # drop 0b prefix and keep last 16 bits
    bin_b = bin(gen['B'])[2:][-16:]

    dec_a = int(bin_a, 2)
    dec_b = int(bin_b, 2)
    diff = dec_a ^ dec_b

    if diff == 0:
        judge_total += 1
        print(f"{x * 100 // total_runs}%")

print(f"Total points by judge: {judge_total}")    
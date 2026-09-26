from collections import defaultdict
import math

# rotation and flip patterns

def to_grid(pattern: str) -> list[str]:
    # convert 'a/b/c' -> ['a', 'b', 'c']
    return pattern.split("/")

def to_pattern(grid: list[str]) -> str:
    # convert ['a', 'b', 'c'] -> 'a/b/c'
    return "/".join(grid)

def flip(grid: list[str]) -> list[str]:
    # mirror each row left-to-right.
    return [row[::-1] for row in grid]

def rotate(grid: list[str]) -> list[str]:
    # rotate 90 degrees clockwise: transpose, then reverse each row.
    n = len(grid)
    return ["".join(grid[n - 1 - c][r] for c in range(n)) for r in range(n)]

def all_orientations(pattern: str) -> set[str]:
    # generate all 8 rotations/flips of a square pattern.
    grid = to_grid(pattern)
    orientations = set()
    for _ in range(4):
        grid = rotate(grid)
        orientations.add(to_pattern(grid))
        orientations.add(to_pattern(flip(grid)))
    return orientations

# build rules into dictionary, account for all orientations

def buildRules(rules: str) -> dict:
    rulesdict = {}
    for rule in rules:
        tmp = rule.split('=>')
        part1 = tmp[0].strip()
        part2 = tmp[1].strip()

        part1_orientations = all_orientations(part1)
        for p1o in part1_orientations:
            rulesdict[p1o] = part2

    return rulesdict

# split the long 4x4-block outputs into 2x2s

def splitPattern(pattern: dict):
    newpattern = defaultdict(int)

    for k,v in pattern.items():
        newpattern[k] += v
        if len(k) == 19 and v > 0:
            tmp = k.split('/')

            # build the blocks one by one
            tmp1 = tmp[0][0:2] + '/' + tmp[1][0:2]
            tmp2 = tmp[0][2:4] + '/' + tmp[1][2:4]
            tmp3 = tmp[2][0:2] + '/' + tmp[3][0:2]
            tmp4 = tmp[2][2:4] + '/' + tmp[3][2:4]

            newpattern[tmp1] += v
            newpattern[tmp2] += v
            newpattern[tmp3] += v
            newpattern[tmp4] += v

            # 4x4 block has been split, so set this original key to 0
            newpattern[k] = 0

    return newpattern

# pattern iteration function

def iteratePattern(pattern: dict, rulesdict: dict) -> dict:
    newpattern = defaultdict(int)

    for k,v in pattern.items():
        if v > 0:
            output = rulesdict[k]
            newpattern[output] += v
            newpattern[k] = 0

    # for all the 4x4 blocks, split into 2x2s
    newpattern = splitPattern(newpattern)

    return newpattern

# count lit blocks

def countLitBlocks(pattern: dict) -> int:
    count = 0
    for k,v in pattern.items():
        tmp = sum([1 if c == '#' else 0 for c in k ]) * v
        count += tmp

    return count
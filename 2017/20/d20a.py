import os
from collections import defaultdict

# class for particle
class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

        self.Pt = defaultdict(list[int])
        self.Pt[0] = p

    def calculatePosition(self, ticks):
        # each tick, velocity at time t [V(t)] is equal to the acceleration amount (A) multiplied by time
        # V(0) is the initial velocity
        # V(0) = V(0)
        # V(1) = V(0) + A
        # V(2) = V(0) + 2A
        # thus, V(t) = V(0) + (A * t)

        # likewise, each tick, the position at time t [P(t)] increases by the velocity at time t [V(t)]
        # Claude helped to generalise the following formula (no coding assistance)
        # P(t) = P(0) + V(0)·t + A·t(t+1)/2
        p_new = [self.Pt[0][0] + (self.v[0] * ticks) + (self.a[0] * ticks * (ticks + 1) * 0.5),
                 self.Pt[0][1] + (self.v[1] * ticks) + (self.a[1] * ticks * (ticks + 1) * 0.5),
                 self.Pt[0][2] + (self.v[2] * ticks) + (self.a[2] * ticks * (ticks + 1) * 0.5)]

        return p_new

    def getPosition(self, ticks):
        if ticks not in self.Pt:
            self.Pt[ticks] = self.calculatePosition(ticks)
        return self.Pt[ticks]
        
    def distanceFromZero(self, ticks):
        p = self.getPosition(ticks)
        return abs(p[0]) + abs(p[1]) + abs(p[2])

# dict for particles
particles = defaultdict(Particle)    

# read input
debug = False
lines = None
if debug:
    lines = open('2017/20/input_sample.txt', 'r').readlines()
else:
    lines = open('2017/20/input.txt', 'r').readlines()

# parse input
def extract_nums(s: str) -> list[int]:
    # trim the 'x=<' at the start and the '>' at the end, split, then cast to int
    nums = [int(x) for x in s[3:-1].split(',')]
    return nums

# create particles and place them into dictionary
for i, line in enumerate(lines):
    parts = line.replace('\n', '').split(', ')
    p = extract_nums(parts[0])
    v = extract_nums(parts[1])
    a = extract_nums(parts[2])

    particle = Particle(p, v, a)
    particles[i] = particle

# assume that after 10000 ticks we have a reasonable guess as to which one is closer to origin point (0, 0, 0)
min_particle, min_dist = None, 99999999
for k, particle in particles.items():
    dist_arbitrary = particle.distanceFromZero(10000)
    if dist_arbitrary < min_dist:
        min_dist = dist_arbitrary
        min_particle = k

# print particle num closest to origin
print(min_particle)
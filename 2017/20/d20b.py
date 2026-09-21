import os
import math
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

def checkCollision(P1: Particle, P2: Particle) -> bool:
    # from part A we already know
    # P(t) = P(0) + V(0)·t + A·t(t+1)/2
    # so we are looking for a situation where P1(t) == P2(t) for some t
    # difference in position is d(t) = P1(t) - P2(t)
    # d(t) = (P1 - P2) + (V1 - V2)t + [(A1 - A2) * t * (t + 1) / 2]
    
    # Again asking Claude to help simplify the math (no coding assistance) yields:
    # α = (Aa - Ab) / 2 
    # β = (Va - Vb) + (Aa - Ab) / 2
    # γ = (Pa - Pb)
    # And the equation becomes a quadratic equation which can be solved for t (positive integers only since ticks only move from 0 -> 1 -> ...):
    # α·t² + β·t + γ = 0

    collide = [False for k in range(3)]
    for k in range(3):
        alpha = (P1.a[k] - P2.a[k]) / 2
        beta = (P1.v[k] - P2.v[k]) + ((P1.a[k] - P2.a[k]) / 2)
        gamma = (P1.p[k] - P2.p[k])

        # handle degenerate cases
        if alpha == 0 and beta == 0:
            # collapses to just an equation no longer in t
            if gamma == 0:
                collide[k] = True
                continue
            else:
                collide[k] = False
                continue

        if alpha == 0 and beta != 0:
            # linear equation
            t = -gamma / beta
            if P1.getPosition(t) == P2.getPosition(t):
                collide[k] = True
                continue
            else:
                continue

        # if edge cases do not apply, proceed with quadratic formula
        # check if value under sqrt is real
        sqrt_val = (beta * beta) - (4 * alpha * gamma)
        if sqrt_val < 0:
            return False

        # if sqrt_val is positive then proceed
        t_pos = (-beta + math.sqrt(sqrt_val)) / (2 * alpha)
        t_neg = (-beta - math.sqrt(sqrt_val)) / (2 * alpha)

        if t_pos > 0 and P1.getPosition(t_pos) == P2.getPosition(t_pos):
            collide[k] = True
            continue

        if t_neg > 0 and P1.getPosition(t_neg) == P2.getPosition(t_neg):
            collide[k] = True
            continue
    
    return all(collide)

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

# check each particle against the other to find collisions
removedParticles = set()
for i in range(len(particles.keys())):
    if i in removedParticles:
        continue

    for j in range(i + 1, len(particles.keys())):
        if j in removedParticles:
            continue

        if i == j:
            print("Fucked up")
        if checkCollision(particles[i], particles[j]):
            removedParticles.add(i)
            removedParticles.add(j)

particlesLeft = len(particles) - len(removedParticles)
print(particlesLeft)
import os
import re
import math

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# define grid size: (11, 7) for sample and (101, 103) for real data
Gx = 101
Gy = 103

# a list for all robots to live in
robots = []

# define a class for the robot guards
class robot:
    def __init__(self, Px, Py, Vx, Vy, Gx, Gy):
        self.Px = Px
        self.Py = Py
        self.Vx = Vx
        self.Vy = Vy
        self.Gx = Gx
        self.Gy = Gy

    def move(self):
        self.Px += self.Vx
        while (self.Px < 0):
            self.Px += self.Gx
        while (self.Px >= self.Gx):
            self.Px -= self.Gx
        
        self.Py += self.Vy
        while (self.Py < 0):
            self.Py += self.Gy
        while (self.Py >= self.Gy):
            self.Py -= self.Gy

        #print('Robot is now at X Y:', self.Px, self.Py)
    
    def get_quadrant(self):
        Mx = int((self.Gx - 1) / 2)
        My = int((self.Gy - 1) / 2)

        #print('Mx, My, Px, Py :', Mx, My, self.Px, self.Py)

        if self.Px < Mx and self.Py < My:
            return 1
        elif self.Px > Mx and self.Py < My:
            return 2
        elif self.Px < Mx and self.Py > My:
            return 3
        elif self.Px > Mx and self.Py > My:
            return 4
        else:
            return 0 # this robot is on one of more of the middle lines and should be ignored

# import data
data = [line.strip() for line in open('input_a.txt', 'r').readlines()]
for line in data:
    nums = re.findall(r'-?\d+', line)
    temp_robot = robot(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]), Gx, Gy)
    robots.append(temp_robot)

# run simulation and keep your eyes peeled for a Christmas tree
treeFound = False
x = -1
while not treeFound:
    x += 1
    G = [[' ' for _ in range(Gx)] for _ in range(Gy)]
    print('Simulating moves at second: ', x + 1)
    for robot in robots:
        robot.move()
        G[robot.Py][robot.Px] = '.'


    # look for a line of continuous pixels and assume that's part of the tree cluster
    # this is stupid, but it works, so it's not stupid
    # visual inspection follows anyway
    for line in range(len(G)):
        to_print = ''.join(G[line])
        if '........' in to_print:
            treeFound = True

    # print out the grid to see the tree!
    if treeFound:
        clear()
        for line in range(len(G)):
            to_print = ''.join(G[line])
            print(to_print)
        print('Found at second: ', x + 1)
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:32:57 2021

@author: eraif
"""

FLASH_COUNT = 0

data = """2344671212
6611742681
5575575573
3167848536
1353827311
4416463266
2624761615
1786561263
3622643215
4143284653""".split()


class octopus:
    def __init__(self, nrg):
        self.energy = nrg
        self.flashed = False
    def __repr__(self):
        if self.flashed == False:
            return ' ' + str(self.energy) + ' '
        else:
            return '*' + str(self.energy) + '*'
    def flash(self):
        self.flashed = True
        self.energy = 0
        return
    def reset_flash(self):
        self.flashed = False
        return
    def increment_energy(self):
        self.energy += 1
        return

class coords:
    def __init__(self, x_in, y_in):
        self.x = x_in
        self.y = y_in
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
            
def step(grid):
    global FLASH_COUNT 
    for row in grid:
        for octo in row:
            octo.increment_energy()
    flashed_in_step = 0
    just_flashed = ["dummy"]
    while len(just_flashed) != 0:
        just_flashed = []
        for j in range(1,len(grid)-1):
            for i in range(1,len(grid[j])-1):
                if grid[j][i].energy > 9 and grid[j][i].flashed == False:
                    grid[j][i].flash()
                    just_flashed.append(coords(i,j))
                    flashed_in_step += 1
                    FLASH_COUNT += 1
        for c in just_flashed:
            increment = (-1, 0, 1)
            for dy in increment:
                for dx in increment:
                    if not grid[c.y + dy][c.x + dx].flashed:
                        grid[c.y + dy][c.x + dx].increment_energy()
    for row in grid:
        for octo in row:
            octo.reset_flash()
    return flashed_in_step
                
        
# -5000 borders creates halo of octopi to make logic easier
octopi = [[octopus(-5000)]*12,[octopus(-5000)]*12]
for line in data:
    octopi.insert(1, [octopus(-500)]*2)
    for i in line:
        octopi[1].insert(1,octopus(int(i)))

all_flashed = False
i = 1
while not all_flashed:
    flashed_in_step = step(octopi)
    if i == 100:
        # Flashes after 100 steps
        print("Part 1:", FLASH_COUNT)
    if flashed_in_step == 100:
        # Step upon which all octopi flash
        print("Part 2:", i)
        all_flashed = True
    i += 1

        

    
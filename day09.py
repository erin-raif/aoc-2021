# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:29:58 2021

@author: eeenr
"""

import numpy as np
from collections import Counter

class coords:
    def __init__(self, x_in, y_in):
        self.x = x_in
        self.y = y_in
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) +")"
    def __eq__(self, o):
        # Could also do this using key
        return (self.x == o.x and self.y == o.y)
    def __key(self):
        return (self.x, self.y)
    def __hash__(self):
        # Make hashable for use with counter
        return hash(self.__key())
    

def find_minima(j,i,levels):
    """ Recursively find co-ordinates for the minima a particular point leads to.
    Note lots of logic holes - relies on the unique formulation of the problem such that
    there are never places where all neighbours are of equal height, and there is only
    one minimum per basin."""
    neighbours = [levels[j][i+1], levels[j][i-1], levels[j-1][i], levels[j+1][i]]
    if min(neighbours) > levels[j][i]:
        return j, i, levels
    else:
        if levels[j][i+1] < levels[j][i]:
            return find_minima(j, i+1, levels)
        elif levels[j][i-1] < levels[j][i]:
            return find_minima(j, i-1, levels)
        elif levels[j+1][i] < levels[j][i]:
            return find_minima(j+1, i, levels)    
        elif levels[j-1][i] < levels[j][i]:
            return find_minima(j-1, i, levels)     

data = open('day09.txt').read().split()

levels = []
for s in data:
    levels.append([])
    for i in s:
        levels[-1].append(int(i))
# Add border of 9s to simplify logic.
for row in levels:
    row.insert(0,9)
    row.append(9)
levels.insert(0,[9]*len(levels[0]))
levels.append([9]*len(levels[0]))

risks = []        
rows = len(levels)
cols = len(levels[0])
# Part 1 - find the sum of risk values (heights of minima + 1)
for j in range(1,rows-1):
    for i in range(1,cols-1):
        neighbours = [levels[j][i+1], levels[j][i-1], levels[j-1][i], levels[j+1][i]]
        if min(neighbours) > levels[j][i]:
            risks.append(levels[j][i] +1)     
print("Part 1:", np.sum(risks))
# Part 2 - find the sizes of the three largest basins and multiply them
minima = []
for j in range(1, rows-1):
    for i in range(1, cols-1):
        if levels[j][i] != 9:
            y, x, _ = find_minima(j,i,levels)
            minima.append(coords(x,y))
# Find most-commonly occuring minima: no. occurrences = basin size
count = Counter(minima)
print("Part 2:", count.most_common(3)[0][1] * count.most_common(3)[1][1] * count.most_common(3)[2][1])
            
    

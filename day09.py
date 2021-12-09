# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:29:58 2021

@author: eeenr
"""

import numpy as np
from scipy.ndimage.filters import minimum_filter
data = open('day09.txt').read().split()

# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split()
levels = []
for s in data:
    levels.append([])
    for i in s:
        levels[-1].append(int(i))


risky = []        
rows = len(levels)
cols = len(levels[0])

for j in range(rows):
    for i in range(cols):
        # Note that indices are of the form j, i
        if i == 0 and j == 0:
            # Top-left corner
            if levels[0][1] > levels[0][0] and levels[1][0] > levels[0][0]:
                risky.append(levels[j][i])
        elif i == 0 and j == rows-1:
            # Bottom-left corner
            if levels[rows-1][1] > levels[rows-1][0] and levels[rows-2][0] > levels[rows-1][0]:
                risky.append(levels[j][i])
        elif i == cols-1 and j == 0:
            # Top-right corner
            if levels[0][cols-2] > levels[0][cols-1] and levels[1][cols-1] > levels[0][cols-1]:
                risky.append(levels[j][i])
        elif i == cols-1 and j == rows-1:
            # Bottom-right corner
            if levels[rows-2][cols-1] > levels[rows-1][cols-1] and levels[rows-1][cols-2] > levels[rows-1][cols-1]:
                risky.append(levels[j][i])
        elif i == 0:
            # Left column, not corner
            neighbours = [levels[j+1][i], levels[j-1][i], levels[j][i+1]]
            if min(neighbours) > levels[j][i]:
                risky.append(levels[j][i])
        elif i == cols-1:
            # Right column, not corner
            neighbours = [levels[j+1][i], levels[j-1][i], levels[j][i-1]]
            if min(neighbours) > levels[j][i]:
                risky.append(levels[j][i])
        elif j == 0:
            # Top row, not corner
            neighbours = [levels[j][i+1], levels[j][i-1], levels[j+1][i]]
            if min(neighbours) > levels[j][i]:
                risky.append(levels[j][i])
        elif j == rows-1:
            # Bottom row, not corner
            neighbours = [levels[j][i+1], levels[j][i-1], levels[j-1][i]]
            if min(neighbours) > levels[j][i]:
                risky.append(levels[j][i])
        else:
            # Somewhere in the middle
            neighbours = [levels[j][i+1], levels[j][i-1], levels[j-1][i], levels[j+1][i]]
            if min(neighbours) > levels[j][i]:
                risky.append(levels[j][i])        

print(np.sum(risky)+len(risky))
            
    
        
        
# levels = np.array(levels)
# minima = (levels == minimum_filter(levels,sizemode='constant',cval=10.0))
# res = np.where(1 == minima)
# risk_sum = 0
# for i in range(len(res[0])):
#     risk_sum += levels[res[0][i],res[1][i]] + 1
# print(risk_sum)
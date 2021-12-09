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
for row in levels:
    row.insert(0,9)
    row.append(9)
levels.insert(0,[9]*len(levels[0]))
levels.append([9]*len(levels[0]))
# print(np.array(levels))

risky = []        
rows = len(levels)
cols = len(levels[0])

for j in range(1,rows-1):
    for i in range(1,cols-1):
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
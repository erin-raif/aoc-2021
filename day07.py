# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:08:53 2021

@author: eeenr
"""

import numpy as np

crabs = open('day07.txt').read().strip('\n').split(',')
crabs = np.array([int(c) for c in crabs], dtype=np.int64)

current_low_p1 = 1e50
current_low_p2 = 1e50

for i in range(np.max(crabs)+1):
    steps = np.abs(crabs - i)
    part_1_cost = np.sum(steps)
    part_2_cost = np.sum(steps*(steps+1)/2)
    if part_1_cost < current_low_p1:
        current_low_p1 = part_1_cost
    if part_2_cost < current_low_p2:
        current_low_p2 = part_2_cost
        
print("Part 1:", current_low_p1)
print("Part 2:", current_low_p2)
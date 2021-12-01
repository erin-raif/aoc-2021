# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:48:39 2021

@author: eeenr
"""

import numpy as np

# Input depths
depths = np.genfromtxt("day01.txt")

# Part 1: Counting the number of times a depth measurement
# increases from the previous measurement
differences = np.diff(depths)
print(np.count_nonzero(differences > 0))

# Part 2: Counting the number of times the depth of the three following
# measurements increases
depths = list(depths)
three_measures = []
for i in range(len(depths)-2):
        three_measures.append(depths[i]+depths[i+1]+depths[i+2])
three_measures = np.array(three_measures)
print(np.count_nonzero(np.diff(three_measures) > 0))
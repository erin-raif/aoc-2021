# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:14:27 2021

@author: eeenr
"""

from collections import Counter

def perform_timestep(count):
    new_count = Counter()
    for i in range(8):
        if i == 0:
            new_count[8] = count[0]
            new_count[6] = count[0]
            new_count[0] = count[1]
        elif i == 6:
            new_count[6] += count[7]
        else:
            new_count[i] = count[i+1]
    return new_count

#fish = [3,4,3,1,2]
fish = open('day06.txt').read().strip('\n').split(',')
fish = [int(f) for f in fish]

c = Counter(fish)
for j in range(256):
    c = perform_timestep(c)
# Because c.total() isn't working for some reason, do sum manually?
s = 0
for i in range(9):
    s += c[i]

print(s)
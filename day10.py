# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:40:39 2021

@author: eraif
"""
import numpy as np
LH_CHAR = ['(','[','{','<']
RH_CHAR = [')',']','}','>']
SCORES = {'(': 1, '[': 2, '{': 3, '<': 4, ')': 3, ']': 57, '}': 1197, '>': 25137}

def check_for_error(line):
    for i in range(len(line)):
        if line[i] not in RH_CHAR and i == len(line)-1:
            return line
        if line[i] in RH_CHAR:
            break
    if LH_CHAR.index(line[i-1]) == RH_CHAR.index(line[i]):
        line = line[:i-1] + line[i+1:]
        return check_for_error(line)
    else:
        return line[i]
data = open('day10.txt').read().split()
incomplete_lines = []
part1 = 0
for line in data:
    e = check_for_error(line)
    if len(e) == 1 and e in RH_CHAR:
        part1 += SCORES[e]
    else:
        incomplete_lines.append(e)
print("Part 1:", part1)
ac_scores = []
for line in incomplete_lines:
    line = line[::-1]
    s = 0
    for char in line:
        s *= 5
        s += SCORES[char]
    ac_scores.append(s)
print("Part 2:", np.median(ac_scores))
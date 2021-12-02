# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:32:13 2021

@author: eeenr
"""

def read_directions(filename):
    file = open(filename)
    directions = []
    for line in file:
        directions.append(line.split())
    # Transpose list of lists so f, u, d in one column
    #directions = list(map(list, zip(*directions)))
    return directions

directions = read_directions("day02.txt")

# Part 1 - find horizontal position and depth if it behaves like you expect

horizontal_position = 0
depth = 0
for i in range(len(directions)):
    if directions[i][0] == "forward":
        horizontal_position += int(directions[i][1])
    elif directions[i][0] == "down":
        depth += int(directions[i][1])
    elif directions[i][0] == "up":
        depth -= int(directions[i][1])

print("Part 1: ", horizontal_position * depth)

# Part 2 - treat up and down as aim
horizontal_position = 0
depth = 0
aim = 0
for i in range(len(directions)):
    if directions[i][0] == "forward":
        horizontal_position += int(directions[i][1])
        depth += aim * int(directions[i][1])
    elif directions[i][0] == "down":
        aim += int(directions[i][1])
    elif directions[i][0] == "up":
        aim -= int(directions[i][1])
        
print("Part 2: ", horizontal_position * depth)
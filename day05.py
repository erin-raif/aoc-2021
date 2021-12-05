# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:14:02 2021

@author: eraif
"""
import numpy as np
def read_data(filename):
    file = open(filename,'r')
    coords = []
    for line in file:
        line = line.strip('\n').split(' -> ')
        lc = []
        for place in line:
            place = place.split(',')
            for x_or_y in place:
                lc.append(int(x_or_y))
        coords.append(lc)
    return coords

def is_orthogonal(coord):
    if coord[0] == coord[2]:
        return True
    elif coord[1] == coord[3]:
        return True
    else:
        return False
    
def plot_orthogonal(grid, coord):
    if coord[0] == coord[2]:
        maxy = max(coord[1],coord[3])
        miny = min(coord[1],coord[3])
        for y in range(miny,maxy+1):
            grid[y,coord[0]] += 1
    else:
        maxx = max(coord[0],coord[2])
        minx = min(coord[0],coord[2])
        for x in range(minx,maxx+1):
            grid[coord[1],x] += 1
            
def is_diagonal(coord):
    if abs(coord[0]-coord[2]) == abs(coord[1]-coord[3]):
        return True
    else:
        return False

def plot_diagonal(grid, coord):
    # Check which "direction" the line runs in and plot accordingly.
    if coord[0] < coord[2]:
        ud = True
    else:
        ud = False
    if coord[1] < coord[3]:
        lr = True
    else:
        lr = False
    for i in range(abs(coord[0]-coord[2])+1):
        if lr == True and ud == True:
            # print("Plot point: ", coord[1]+i,coord[0]+i)
            grid[coord[1]+i,coord[0]+i] += 1
        elif lr == True and ud == False:
            # print("Plot point: ", coord[1]+i,coord[0]-i)
            grid[coord[1]+i,coord[0]-i] += 1
        elif lr == False and ud == True:
            # print("Plot point: ", coord[1]-i,coord[0]+i)
            grid[coord[1]-i,coord[0]+i] += 1
        elif lr == False and ud == False:
            # print("Plot point: ", coord[1]-i,coord[0]-i)
            grid[coord[1]-i,coord[0]-i] += 1
            
    
    
coords = read_data('day05.txt')
grid_max  = np.max(np.array(coords))

grid = np.zeros((grid_max+1,grid_max+1))

orthogonal_coords = []
for c in coords:
    if is_orthogonal(c):
        plot_orthogonal(grid, c)
# print(grid)
print("Part 1:", np.count_nonzero(grid >= 2))
for c in coords:
    # print(c)
    if is_diagonal(c):
        plot_diagonal(grid, c)
        # print(grid)
    # else:
        # print("No line plotted")
print("Part 2:", np.count_nonzero(grid >= 2))
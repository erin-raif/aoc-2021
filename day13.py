# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:45:25 2021

@author: eeenr
"""
import matplotlib.pyplot as plt
coordinates_in, folds_in = open('day13.txt').read().split('\n\n')

class fold_line:
    def __init__(self, d_in, c_in):
        self.d = d_in # direction
        self.c = int(c_in) # coordinate
    def __repr__(self):
        return "fold along " + self.d + "=" + str(self.c)

class dot:
    def __init__(self, x_in, y_in):
        self.x = int(x_in)
        self.y = int(y_in)
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) +")"
    def __eq__(self, o):
        return (self.x == o.x and self.y == o.y)
    def __key(self):
        return (self.x, self.y)
    def __hash__(self):
        # Make hashable for use with counter
        return hash(self.__key())
    
def fold_along_x(dots,line):
    new_dots = []
    for d in dots:
        if d.x < line:
            new_dots.append(d)
        else:
            new_x = line - (d.x - line)
            new_dots.append(dot(new_x, d.y))
    return set(new_dots)

def fold_along_y(dots,line):
    new_dots = []
    for d in dots:
        if d.y < line:
            new_dots.append(d)
        else:
            new_y = line - (d.y - line)
            new_dots.append(dot(d.x, new_y))
    return set(new_dots)
    
dots = []
for line in coordinates_in.split('\n'):
    dots.append(dot(line.split(',')[0],line.split(',')[1]))
dots = set(dots)
folds = []
for line in folds_in.split('\n'):
    folds.append(fold_line(line[11],line[13:]))

new_dots = fold_along_x(dots, folds[0].c)
print("Part 1:", len(new_dots))

for f in folds[:]:
    if f.d == 'x':
        dots = fold_along_x(dots, f.c)
    elif f.d == 'y':
        dots = fold_along_y(dots, f.c)
    
x_coords = [d.x for d in dots]
y_coords = [d.y for d in dots]

plt.scatter(x_coords,y_coords)
# For some reason, this produces the result upside-down!
plt.show()

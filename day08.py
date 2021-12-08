# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:06:54 2021

@author: eeenr
"""

class entry:
    def __init__(self, sig_in, output_in):
        self.signal = sig_in
        self.output = output_in
        self.sort_signal_lengths()
        self.calculate_bindings()
        self.map_bindings()
        self.calc_output_number()
    def __repr__(self):
        string = "Signal: "
        for s in self.signal:
            string += s + " "
        string += "\nOutput: "
        for o in self.output:
            string += o + " "
        return string
    def sort_signal_lengths(self):
        self.signal_length_six = []
        for s in self.signal:
            if len(s) == 2:
                self.signal_one = set(s)
            elif len(s) == 3:
                self.signal_seven = set(s)
            elif len(s) == 4:
                self.signal_four = set(s)
            elif len(s) == 6:
                self.signal_length_six.append(set(s))
            elif len(s) == 7:
                self.signal_eight = set(s)
    def output_sets(self):
        print(self.signal_one, self.signal_seven, self.signal_four,
                  self.signal_eight, self.signal_length_six)
    def calculate_bindings(self):
        # self.output_sets()
        # top = t, c = centre, b = bottom
        self.t = self.signal_seven.difference(self.signal_one)
        self.tl_c = self.signal_four.difference(self.signal_one)
        self.r = self.signal_four.difference(self.tl_c)
        self.bl_b = self.signal_eight.difference(self.t.union(self.tl_c, self.r))
        # print("T: ", self.t, "TL/C: ", self.tl_c, "R: ", self.r, "BL/B: ", self.bl_b)
        for s in self.signal_length_six:
            if self.signal_eight.difference(s).issubset(self.tl_c):
                self.c = self.signal_eight.difference(s)
                self.tl = self.tl_c.difference(self.c)
            elif self.signal_eight.difference(s).issubset(self.r):
                self.tr = self.signal_eight.difference(s)
                self.br = self.r.difference(self.tr)
            elif self.signal_eight.difference(s).issubset(self.bl_b):
                self.bl = self.signal_eight.difference(s)
                self.b = self.bl_b.difference(self.bl)
        # self.output_bindings()
    def output_bindings(self):
        print("T: ", self.t, "TR: ", self.tr, "BR: ",
                  self.br, "B: ", self.b, "BL: ", self.bl, 
                      "TL: ", self.tl, "C: ", self.c)
    def map_bindings(self):
        self.bindings = {
            frozenset(self.signal_eight - self.c) : 0,
            frozenset(self.signal_one) : 1,
            frozenset(self.t | self.tr | self.c | self.bl | self.b) : 2,
            frozenset(self.t | self.tr | self.c | self.br | self.b) : 3,
            frozenset(self.signal_four) : 4,
            frozenset(self.t | self.tl | self.c | self.br | self.b) : 5,
            frozenset(self.signal_eight - self.tr) : 6,
            frozenset(self.signal_seven) : 7,
            frozenset(self.signal_eight) : 8,
            frozenset(self.signal_eight - self.bl) : 9
        }
    def calc_output_number(self):
        output_digits = len(self.output)
        self.output_number = 0
        for i in range(output_digits):
            self.output_number += (self.bindings[frozenset(self.output[i])] *
                                   (10 ** (output_digits - 1 - i)))

f = open('day08.txt')
entries = []
for line in f:
    line = line.strip('\n').split(" | ")
    entries.append(entry(line[0].split(' '),line[1].split(' ')))

counter = 0
output_sum = 0
for e in entries:
    output_sum += e.output_number
    for o in e.output:
        if len(o) in (2,3,4,7):
            counter += 1

print("Part 1:", counter)
print("Part 2:", output_sum)
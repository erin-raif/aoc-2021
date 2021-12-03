# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:22:38 2021

@author: eeenr
"""

def read_bin_as_str(filename):
    file = open(filename)
    binaries = []
    for line in file:
        binaries.append(line.strip())
    file.close()
    return binaries

def bin_to_dec(list_of_bits):
    size = len(list_of_bits)
    decimal = 0
    for i in range(size):
        if list_of_bits[i] == '1':
            decimal += 2**(size-i-1)
    return decimal

def invert_binary(binary):
    inverted = ''
    for i in range(len(binary)):
        if binary[i] == '1':
            inverted += '0'
        else:
            inverted += '1'
    return inverted

def progressive_search(data_copy, bin_num_length, greater):
    # if bit == '0':
    #     count_list = list(threshold - np.array(count_list))
    threshold = 500
    data = data_copy.copy()
    string = ''
    for i in range(bin_num_length):
        print("Search Threshold:", threshold)
        number_of_ones = 0
        for j in range(len(data)):
            if data[j][i] == '1':
                number_of_ones += 1
        print("Number of ones in position", i+1, ":", number_of_ones)
        indices_to_pop = []
        if greater == True:
            if number_of_ones >= threshold:
                string += '1'
                print("Removing items with 0 in position", i+1)
                for j in range(len(data)):
                    if data[j][i] == '0':
                        indices_to_pop.insert(0,j)
            else:
                string += '0'
                print("Removing items with 1 in position", i+1)
                for j in range(len(data)):
                    if data[j][i] == '1':
                        indices_to_pop.insert(0,j)
        else:
            if number_of_ones < threshold:
                string += '1'
                print("Removing items with 0 in position", i+1)
                for j in range(len(data)):
                    if data[j][i] == '0':
                        indices_to_pop.insert(0,j)
            else:
                string += '0'
                print("Removing items with 1 in position", i+1)
                for j in range(len(data)):
                    if data[j][i] == '1':
                        indices_to_pop.insert(0,j)
        for k in indices_to_pop:
            data.pop(k)      
        print("All remaining strings begin with", string)
        threshold = len(data)/2.0
        if len(data) == 1:
            print("Only one remains!")
            break
        print("\nItems left:", len(data))
    print("Final result:", data[0])
    return data[0]
            
    
data = read_bin_as_str('day03.txt')

# Find frequency of each bit in the binary numbers being 1

bin_num_length = 12
count_list = [0]*bin_num_length
length_bin_list = len(data)

for i in range(length_bin_list):
    for j in range(bin_num_length):
        if data[i][j] == '1':
            count_list[j] += 1

print(count_list)

# Part 1: calculate epsilon and gamma 

epsilon = ''
gamma = ''

for i in count_list:
    if int(i) > length_bin_list/2:
        epsilon += '1'
        gamma += '0'
    else:
        gamma += '1'
        epsilon += '0'

print(bin_to_dec(gamma)*bin_to_dec(epsilon))

# Part 2: calculate LS and O2 rating
print("Common Search")
common = progressive_search(data, bin_num_length, True)
print("\nRare Search")
rare = progressive_search(data, bin_num_length, False)
# Ensure newline character is stripped from strings.
print(bin_to_dec(common) * bin_to_dec(rare))
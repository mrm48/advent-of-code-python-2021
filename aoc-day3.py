#!/usr/bin/env python

mcb = 0
lcb = 0
pos = 2
epsilon = '0b'
gamma = '0b'
result = 0

columns = ['0b','0b','0b','0b','0b']

diag = ['0b00100', '0b11110', '0b10110', '0b10111', '0b10101', '0b01111', '0b00111', '0b11100', '0b10000', '0b11001', '0b00010', '0b01010']

for rep in diag:
    pos = 2
    while (pos < len(rep)):
        nextnum = rep[pos:pos+1]
        columns[pos-2] += nextnum
        pos += 1

for column in columns:
    num_zeroes = column.count('0') - 1
    num_ones = column.count('1')
    if num_zeroes > num_ones:
        mcb = 0
        lcb = 1
    else:
        lcb = 0
        mcb = 1
    epsilon += str(lcb)
    gamma += str(mcb)

print ("epsilon is", epsilon)
print ("gamma is", gamma)
result = int(epsilon, 2)
result = result * int(gamma, 2)
print("Result is", result)

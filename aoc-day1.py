#!/usr/bin/env python

depth_tracker = 0
number_inc = 0
num_elements = 0

depths = [199,200,208,210,200,207,240,269,260,263]

for depth in depths:

    if (depth < depth_tracker and num_elements != 0):
        print(depth, " decreased")
    elif (depth > depth_tracker and num_elements != 0):
        print(depth, " increased")
        number_inc += 1
    else:
        print(depth, " N/A - no previous measurement")

    depth_tracker = depth
    num_elements += 1

print ("Depth increased", number_inc, "times")

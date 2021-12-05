#!/usr/bin/env python

depth = 0
pos = 0

helm = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

for direction in helm:
    dirtemp = direction[0:direction.rfind(" ")]
    numtemp = direction[direction.rfind(" "):len(direction)]
    match dirtemp:
        case "forward":
                pos += int(numtemp)
        case "up":
                depth -= int(numtemp)
        case "down":
                depth += int(numtemp)

print("Sub is at depth %d at location %d" % (depth, pos))

print("Sub is at position", depth * pos)

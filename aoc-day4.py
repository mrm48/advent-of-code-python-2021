#!/usr/bin/env python

callouts = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
board1 = [[22,13,17,11,0], [8,2,23,4,24], [21,9,14,16,7], [6,10,3,18,5],[1,12,20,15,19]]
board2 = [[3,15,0,2,22], [9,18,13,17,5], [19,8,7,25,23], [20,11,10,24,4], [14,21,16,12,6]]
board3 = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5], [2,0,12,3,7]]
board4 = [[7,21,17,24,4], [4,16,15,9,19], [9,8,23,26,20], [5,11,13,6,5], [11,0,12,3,7]]
boards = [board1, board2, board3]
num_items = [0,1,2,3,4]

called = []

def update_board():
    print("")

def check_columns():
    win = False
    for row in num_items:
        if ((board4[row][0] in called) and (board4[row][1] in called) and (board4[row],[2] in called) and (board4[row],[3] in called) and (board4[row],[4] in called)):
            win = True
    return win

for callout in callouts:
    called.append(callout)
    print(called)
    print(check_columns())

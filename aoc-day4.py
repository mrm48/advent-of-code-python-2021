#!/usr/bin/env python

callouts = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
board1 = [[22,13,17,11,0], [8,2,23,4,24], [21,9,14,16,7], [6,10,3,18,5],[1,12,20,15,19]]
board2 = [[3,15,0,2,22], [9,18,13,17,5], [19,8,7,25,23], [20,11,10,24,4], [14,21,16,12,6]]
board3 = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5], [2,0,12,3,7]]
num_items = [0,1,2,3,4]

called = []
win_score = 0

def update_board():
    print("")

def check_columns(board):
    win = False
    for row in num_items:
        if ((board[row][0] in called) and (board[row][1] in called) and (board[row][2] in called) and (board[row][3] in called) and (board[row][4] in called)):
            win=score_rows(board,row,"rows")
    return win

def check_rows(board):
    win = 0
    for column in num_items:
        if ((board[0][column] in called) and (board[1][column] in called) and (board[2][column] in called) and (board[3][column] in called) and (board[4][column] in called)):
            win = score_rows(board, column, "columns")
    return win

def score_rows(board, rows, win):
    win_score = 0
    if win == "columns":
        for row in num_items:
            for col in num_items:
                if col != rows:
                    if not board[row][col] in called:
                        win_score += board[row][col]
    else:
        for row in num_items:
            if row != rows:
               for col in num_items:
                    if not board[row][col] in called:
                        win_score += board[row][col]

    print("Win score:", win_score)
    return win_score

for callout in callouts:
    called.append(callout)
    print(called)
    winner = ""
    board1_win = check_columns(board1)
    if (board1_win != 0):
        win_score = board1_win
        winner = "board1"
    board1_win = check_rows(board1)
    if (board1_win != 0):
        win_score = board1_win
        winner = "board1"
    board2_win = check_columns(board2)
    if (board2_win != 0):
        win_score = board2_win
        winner = "board2"
    board2_win = check_rows(board2)
    if (board2_win != 0):
        win_score = board2_win
        winner = "board2"
    board3_win = check_columns(board3)
    if (board3_win != 0):
        win_score = board3_win
        winner = "board3"
    board3_win = check_rows(board3)
    if (board3_win != 0):
        win_score = board3_win
        winner = "board3"

    if len(winner):
        print ("Winner ", winner, "with score", win_score * callout)
        break

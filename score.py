#!/usr/bin/env python3

import copy
import check_win

SCORE_4_ROW = [0, 2000000, 5000000] #score as 4 in a row, 0 if no open ends, 100000 if 1 and 2000000 if two
SCORE_3_ROW = [0, 30000, 800000] # score 3 in a row
SCORE_2_ROW = [0, 1000, 9000] # score 2 in a row

def four_in_a_row_line(board, i, j, checking):
    if j + 4 > len(board):
        return [False]
    if board[i][j + 1] == checking and board[i][j + 2] == checking and board[i][j + 3] == checking:
        #open ends
        open_ends = 0
        if j + 4 < len(board) and board[i][j + 4] == 0:
            open_ends += 1
        if j - 1 >= 0 and board[i][j - 1] == 0:
            open_ends += 1
        return [True, SCORE_4_ROW[open_ends]]
    return [False]

def three_in_a_row_line(board, i, j, checking):
    if j + 3 > len(board):
        return [False]
    if board[i][j + 1] == checking and board[i][j + 2] == checking:
        #open ends
        open_ends = 0
        check_left = j
        while check_left - 1 >= 0:
            if board[i][check_left - 1] != 0 and board[i][check_left - 1] != checking:
                break
            check_left -= 1
        check_right = j + 2
        while check_right + 1 < len(board):
            if board[i][check_right + 1] != 0 and board[i][check_right + 1] != checking:
                break
            check_right += 1
        if check_right - check_left < 4:
            return [True, 0]
        if j - 1 >= 0 and board[i][j - 1] == 0:
            open_ends += 1
        if j + 3 < len(board) and board[i][j + 3] == 0:
            open_ends += 1
        return [True, SCORE_3_ROW[open_ends]]
    return [False]

def two_in_a_row_line(board, i, j, checking):
    if j + 2 > len(board):
        return [False]
    if board[i][j + 1] == checking:
        #open ends
        open_ends = 0
        check_left = j
        while check_left - 1 >= 0:
            if board[i][check_left - 1] != 0 and board[i][check_left - 1] != checking:
                break
            check_left -= 1
        check_right = j + 1
        while check_right + 1 < len(board):
            if board[i][check_right + 1] != 0 and board[i][check_right + 1] != checking:
                break
            check_right += 1
        if check_right - check_left < 4:
            return [True, 0]
        if j - 1 >= 0 and board[i][j - 1] == 0:
            open_ends += 1
        if j + 2 < len(board) and board[i][j + 2] == 0:
            open_ends += 1
        return [True, SCORE_2_ROW[open_ends]]
    return [False]

def calc_score_line(board, checking):
    score = 0
    j = 0
    for i in range(len(board)):
        while j < len(board):
            if board[i][j] != checking:
                j += 1
                continue
            #calc pawns on board to opti
            #check win
            arr = four_in_a_row_line(board, i, j, checking)
            if arr[0] == True:
                score += arr[1]
                j += 4
                continue
            arr = three_in_a_row_line(board, i, j, checking)
            if arr[0] == True:
                score += arr[1]
                j += 3
                continue
            if score < 10000:
                arr = two_in_a_row_line(board, i, j, checking)
                if arr[0] == True:
                    score += arr[1]
                    j += 2
                    continue
            j += 1
        j = 0
    return score

def four_in_a_row_diag(board, i, j, checking):
    if j + 4 > len(board):
        return [False]
    if i + 4 > len(board):
        return [False]
    if board[i + 1][j + 1] == checking and board[i + 2][j + 2] == checking and board[i + 3][j + 3] == checking:
        #open ends
        open_ends = 0
        if j + 4 < len(board) and i + 4 < len(board) and board[i + 4][j + 4] == 0:
            open_ends += 1
        if j - 1 >= 0 and i - 1 >= 0 and board[i - 1][j - 1] == 0:
            open_ends += 1
        board[i][j] = 0
        board[i + 1][j + 1] = 0
        board[i + 2][j + 2] = 0
        board[i + 3][j + 3] = 0
        return [True, SCORE_4_ROW[open_ends]]
    return [False]

def two_in_a_row_diag(board, i, j, checking):
    if j + 2 > len(board):
        return [False]
    if i + 2 > len(board):
        return [False]
    if board[i + 1][j + 1] == checking:
        #open ends
        open_ends = 0
        check_left = j
        check_second_left = i
        while check_left - 1 >= 0:
            if check_second_left - 1 < 0:
                break
            if board[check_second_left - 1][check_left - 1] != 0 and board[check_second_left - 1][check_left - 1] != checking:
                break
            check_second_left -= 1
            check_left -= 1
        check_right = j + 1
        check_second_right = i + 1
        while check_right + 1 < len(board):
            if check_second_right + 1 >= len(board):
                break
            if board[check_second_right + 1][check_right + 1] != 0 and board[check_second_right + 1][check_right + 1] != checking:
                break
            check_right += 1
            check_second_right += 1
        if check_right - check_left < 4:
            board[i][j] = 0
            board[i + 1][j + 1] = 0
            return [True, 0]
        if j - 1 >= 0 and i - 1 >= 0 and board[i - 1][j - 1] == 0:
            open_ends += 1
        if j + 2 < len(board) and i + 2 < len(board) and board[i + 2][j + 2] == 0:
            open_ends += 1
        board[i][j] = 0
        board[i + 1][j + 1] = 0
        return [True, SCORE_2_ROW[open_ends]]
    return [False]

def three_in_a_row_diag(board, i, j, checking):
    if j + 3 > len(board):
        return [False]
    if i + 3 > len(board):
        return [False]
    if board[i + 1][j + 1] == checking and board[i + 2][j + 2] == checking:
        #open ends
        open_ends = 0
        check_left = j
        check_second_left = i
        while check_left - 1 >= 0:
            if check_second_left - 1 < 0:
                break
            if board[check_second_left - 1][check_left - 1] != 0 and board[check_second_left - 1][check_left - 1] != checking:
                break
            check_second_left -= 1
            check_left -= 1
        check_right = j + 2
        check_second_right = i + 2
        while check_right + 1 < len(board):
            if check_second_right + 1 >= len(board):
                break
            if board[check_second_right + 1][check_right + 1] != 0 and board[check_second_right + 1][check_right + 1] != checking:
                break
            check_right += 1
            check_second_right += 1
        if check_right - check_left < 4:
            board[i][j] = 0
            board[i + 1][j + 1] = 0
            board[i + 2][j + 2] = 0
            return [True, 0]
        if j - 1 >= 0 and i - 1 >= 0 and board[i - 1][j - 1] == 0:
            open_ends += 1
        if j + 3 < len(board) and i + 3 < len(board) and board[i + 3][j + 3] == 0:
            open_ends += 1
        board[i][j] = 0
        board[i + 1][j + 1] = 0
        board[i + 2][j + 2] = 0
        return [True, SCORE_3_ROW[open_ends]]
    return [False]

def calc_score_diag(board, checking):
    new_board = copy.deepcopy(board)
    score = 0
    for i in range(len(new_board)):
        for j in range(len(new_board)):
            if new_board[i][j] != checking:
                continue
            arr = four_in_a_row_diag(new_board, i, j, checking)
            if arr[0] == True:
                score += arr[1]
                continue
            arr = three_in_a_row_diag(new_board, i, j, checking)
            if arr[0] == True:
                score += arr[1]
                continue
            if score < 10000:
                arr = two_in_a_row_diag(new_board, i, j, checking)
                if arr[0] == True:
                    score += arr[1]
                    continue
    return score

def calc_score(board, checking):
    return calc_score_line(board, checking) + calc_score_line(list(zip(*reversed(board))), checking) + calc_score_diag(board, checking) + calc_score_diag([list(item) for item in list(zip(*reversed(board)))], checking)
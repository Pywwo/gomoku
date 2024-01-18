#!/usr/bin/env python3

SCORE_4_ROW = [0, 2000000, 5000000]  # Score as 4 in a row
SCORE_3_ROW = [0, 30000, 800000]  # Score 3 in a row
SCORE_2_ROW = [0, 1000, 9000]  # Score 2 in a row

def in_bounds(i, j, size):
    return 0 <= i < size and 0 <= j < size

def in_a_row_line(board, i, j, checking, length):
    if j + length > len(board):
        return [False]
    for k in range(1, length):
        if board[i][j + k] != checking:
            return [False]
    return [True, 0]

def in_a_row_diag(board, i, j, checking, length, direction):
    if j + length * direction[1] > len(board) or i + length * direction[0] > len(board):
        return [False]
    for k in range(1, length):
        if board[i + k * direction[0]][j + k * direction[1]] != checking:
            return [False]
    return [True, 0]

def calc_score_line(board, checking, scores):
    size = len(board)
    score = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != checking:
                continue
            for length, score_value in enumerate(scores[1:], start=1):
                if in_bounds(i, j + length, size):
                    arr = in_a_row_line(board, i, j, checking, length + 1)
                    if arr[0]:
                        score += score_value
            for length, score_value, direction in zip(range(1, 4), scores[1:], [(1, 0), (0, 1), (1, 1)]):
                if in_bounds(i + length, j + length, size):
                    arr = in_a_row_diag(board, i, j, checking, length + 1, direction)
                    if arr[0]:
                        score += score_value
    return score

def calc_score(board, checking):
    return (calc_score_line(board, checking, SCORE_4_ROW) +
            calc_score_line(list(zip(*reversed(board))), checking, SCORE_4_ROW) +
            calc_score_line(board, checking, SCORE_3_ROW) +
            calc_score_line(list(zip(*reversed(board))), checking, SCORE_3_ROW) +
            calc_score_line(board, checking, SCORE_2_ROW) +
            calc_score_line(list(zip(*reversed(board))), checking, SCORE_2_ROW) +
            calc_score_line(list(zip(*reversed(board))), checking, SCORE_2_ROW) +
            calc_score_line(board, checking, SCORE_2_ROW))

#!/usr/bin/env python3

def check_line(array, checking, start, step, sizemax):
    end = start + 5 * step
    if end < 0 or end > sizemax:
        return False
    return all(array[i][j] == checking for i, j in zip(range(start, end, step), [start] * 5))

def check_win_five(array, checking):
    sizemax = len(array)
    for i in range(sizemax):
        for j in range(len(array[0])):
            if array[i][j] == checking:
                if any(check_line(array, checking, j, 1, sizemax),
                       check_line(array, checking, i, 1, sizemax),
                       check_line(array, checking, j - i, 1, sizemax),
                       check_line(array, checking, i + j, -1, sizemax)):
                    return True
    return False

#!/usr/bin/env python3

def check_vertically(array, checking, i, j, sizemax):
    a = i
    while a < i + 5:
        if a >= sizemax:
            return False
        if array[a][j] != checking:
            return False
        a += 1
    return True

def check_horizontally(array, checking, i, j, sizemax):
    a = j
    while a < j + 5:
        if a >= sizemax:
            return False
        if array[i][a] != checking:
            return False
        a += 1
    return True

def check_diagonally_left(array, checking, i, j, sizemax):
    if j - 5 < 0 or i + 5 > sizemax:
        return False
    a = 0
    while a < 5:
        if array[i + a][j - a] != checking:
            return False
        a += 1
    return True

def check_diagonally_right(array, checking, i, j, sizemax):
    if j + 5 > sizemax or i + 5 > sizemax:
        return False
    a = 0
    while a < 5:
        if array[i + a][j + a] != checking:
            return False
        a += 1
    return True

def check_win_five(array, checking):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == checking:
                if check_horizontally(array, checking, i, j, len(array)) == True:
                    return True
                if check_vertically(array, checking, i, j, len(array)) == True:
                    return True
                if check_diagonally_left(array, checking, i, j, len(array)) == True:
                    return True
                if check_diagonally_right(array, checking, i, j, len(array)) == True:
                    return True
    return False
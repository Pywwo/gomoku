#!/usr/bin/env python3

import sys

#import of the file we are going to test
sys.path.append('../')
import check_win
import score

def test_check_win_true():
    board = []
    for i in range(5):
        board.append([0] * 5)
    board[0] = [1, 1, 1, 1, 1]
    assert check_win.check_win_five(board, 1) == True, "Should be True"
    print ("test : check_win_true PASSED")

def test_check_win_false():
    board = []
    for i in range(5):
        board.append([0] * 5)
    board[0] = [1, 1, 1, 1, 0]
    assert check_win.check_win_five(board, 1) == False, "Should be False"
    print ("test : check_win_false PASSED")

def test_all_score():
    board = []
    for i in range(5):
        board.append([0] * 5)
    board[0] = [0, 1, 1, 0, 0]
    assert score.calc_score(board, 1) == 9000, "Sould be 9000"
    print ("test : score with 2 PASSED")
    board[0] = [0, 1, 1, 1, 0]
    assert score.calc_score(board, 1) == 800000, "Sould be 800000"
    print ("test : score with 3 PASSED")
    board[0] = [0, 1, 1, 1, 1]
    assert score.calc_score(board, 1) == 2000000, "Sould be 2000000"
    print ("test : score with 4 PASSED")
    board[0] = [0, 1, 1, 1, 2]
    assert score.calc_score(board, 1) == 0, "Sould be 0"
    print ("test : no score while blocked PASSED")

def unit_test():
    #testing check_win
    try:
        test_check_win_true()
    except AssertionError as error:
        print ("ERROR : " + str(error))
        return
    try:
        test_check_win_false()
    except AssertionError as error:
        print ("ERROR : " + str(error))
        return
    #testing score
    try:
        test_all_score()
    except AssertionError as error:
        print ("ERROR : " + str(error))
        return

if __name__=='__main__':
    unit_test()
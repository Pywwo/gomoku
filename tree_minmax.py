#!/usr/bin/env python3

import score
import check_win

class Tree:
    def __init__(self, player, depth, board):
        self._max_depth = depth
        self._board = board
        self._min_score_array = []
        self._max_score_array = []
        self.i_can_end = False
        self.he_can_end = False
        self.my_end_move = []
        self.his_end_move = []
        if self.check_win_possibility() == False:
            self.tree_creator(board, player, depth, 0, 0)

    def check_win_possibility(self):
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] != 0:
                    continue
                self._board[i][j] = 1
                if check_win.check_win_five(self._board, 1) == True:
                    self.i_can_end = True
                    self.my_end_move =  [float('inf'), i, j, 0, 0]
                    return True
                self._board[i][j] = 0
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] != 0:
                    continue
                self._board[i][j] = 2
                if check_win.check_win_five(self._board, 2) == True:
                    self.he_can_end = True
                    self.his_end_move =  [float('-inf'), i, j, 0, 0]
                    return True
                self._board[i][j] = 0
        return False

    def tree_creator(self, board, current_player, depth, saved_i, saved_j):
        min_score = None
        max_score = None
        other_player = current_player + 1
        if other_player > 2:
            other_player = 1
        if depth == 0:
            return
        if depth == 1:
            saved_score = score.calc_score(board, 1)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 0:
                    continue
                if self.no_pawn_around(board, i, j) == True:
                    continue
                board[i][j] = current_player
                self.tree_creator(board, other_player, depth - 1, i, j)
                if depth == 1:
                    #calc score
                    if min_score == None:
                        tmp_score = saved_score - score.calc_score(board, 2) * 0.8
                        min_score = [tmp_score, saved_i, saved_j, i, j]
                        max_score = [tmp_score, saved_i, saved_j, i, j]
                    else:
                        tmp = saved_score - score.calc_score(board, 2) * 0.8
                        if tmp < min_score[0]:
                            min_score = [tmp, saved_i, saved_j, i, j]
                        if tmp > max_score[0]:
                            max_score = [tmp, saved_i, saved_j, i, j]
                board[i][j] = 0
        if depth == 1:
            self._min_score_array.append(min_score)
            self._max_score_array.append(max_score)

    def get_minmax_score(self):
        if sum(sum(self._board,[])) == 0:
            return [0, int(len(self._board) / 2), int(len(self._board) / 2), 0, 0]
        if self.i_can_end == True:
            return self.my_end_move
        if self.he_can_end == True:
            return self.his_end_move
        all_zeros = True
        for i in self._min_score_array:
            if i[0] != 0:
                all_zeros = False
                break
        if all_zeros == True:
            #take best score
            tmp_best_score = 0
            index = 0
            saved_index = 0
            while index < len(self._max_score_arra):
                if tmp_best_score < self._max_score_arra[index][0]:
                    tmp_best_score = self._max_score_arra[index][0]
                    saved_index = index
                index += 1
            return self._max_score_arra[saved_index]
        tmp_score = float('-inf')
        index = 0
        saved_index = 0
        while index < len(self._min_score_array):
            if (tmp_score < self._min_score_array[index][0]):
                tmp_score = self._min_score_array[index][0]
                saved_index = index
            index += 1
        return self._min_score_array[saved_index]

    def no_pawn_around(self, array, i, j):
        #top-left
        if i - 1 >= 0 and j - 1 >= 0 and array[i - 1][j - 1] != 0:
            return False
        #top
        if i - 1 >= 0 and array[i - 1][j] != 0:
            return False
        #top right
        if i - 1 >= 0 and j + 1 < len(array) and array[i - 1][j + 1] != 0:
            return False
        #left
        if j - 1 >= 0 and array[i][j - 1] != 0:
            return False
        #right
        if j + 1 < len(array) and array[i][j + 1] != 0:
            return False
        #bottom left
        if j - 1 >= 0 and i + 1 < len(array) and array[i + 1][j - 1] != 0:
            return False
        #bottom
        if i + 1 < len(array) and array[i + 1][j] != 0:
            return False
        #bottom right
        if i + 1 < len(array) and j + 1 < len(array) and array[i + 1][j + 1] != 0:
            return False
        return True
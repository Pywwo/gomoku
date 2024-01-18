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
        if not self.check_win_possibility():
            self.tree_creator(board, player, depth, 0, 0)

    def check_win_possibility(self):
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] == 0:
                    self._board[i][j] = 1
                    if check_win.check_win_five(self._board, 1):
                        self.i_can_end = True
                        self.my_end_move = [float('inf'), i, j, 0, 0]
                        return True
                    self._board[i][j] = 0

        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] == 0:
                    self._board[i][j] = 2
                    if check_win.check_win_five(self._board, 2):
                        self.he_can_end = True
                        self.his_end_move = [float('-inf'), i, j, 0, 0]
                        return True
                    self._board[i][j] = 0

        return False

    def tree_creator(self, board, current_player, depth, saved_i, saved_j):
        other_player = 3 - current_player
        if depth == 0:
            return

        if depth == 1:
            saved_score = score.calc_score(board, 1)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0 and not self.no_pawn_around(board, i, j):
                    board[i][j] = current_player
                    self.tree_creator(board, other_player, depth - 1, i, j)

                    if depth == 1:
                        tmp_score = saved_score - score.calc_score(board, 2) * 0.8
                        move = [tmp_score, saved_i, saved_j, i, j]

                        if self._min_score_array:
                            if tmp_score < self._min_score_array[0][0]:
                                self._min_score_array = [move]
                            elif tmp_score == self._min_score_array[0][0]:
                                self._min_score_array.append(move)
                        else:
                            self._min_score_array = [move]

                        if not self._max_score_array or tmp_score > self._max_score_array[0][0]:
                            self._max_score_array = [move]
                        elif tmp_score == self._max_score_array[0][0]:
                            self._max_score_array.append(move)

                    board[i][j] = 0

    def get_minmax_score(self):
        if sum(sum(self._board, [])) == 0:
            return [0, len(self._board) // 2, len(self._board) // 2, 0, 0]

        if self.i_can_end:
            return self.my_end_move

        if self.he_can_end:
            return self.his_end_move

        if not self._min_score_array:
            return self._max_score_array[0]

        return self._min_score_array[-1] if self._min_score_array[-1][0] > self._max_score_array[0][0] else self._max_score_array[0]

    def no_pawn_around(self, array, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(array) and 0 <= nj < len(array[0]) and array[ni][nj] != 0:
                return False
        return True

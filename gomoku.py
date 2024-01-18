#!/usr/bin/env python3

import sys
import tree_minmax

ENEMY = 2
ME = 1
board = []

def start(size):
    global Start, board
    if size < 5 or size > 20:
        print("ERROR unsupported size", flush=True)
    else:
        Start = True
        board = [[0] * size for _ in range(size)]
        print("OK", flush=True)

def answer():
    global board

    tmp_tree = tree_minmax.Tree(1, 2, board)
    to_play = tmp_tree.get_minmax_score()
    board[to_play[1]][to_play[2]] = 1
    print("{},{}".format(to_play[2], to_play[1]), flush=True)

def begin():
    answer()

def turn(x, y):
    global board
    board[y][x] = ENEMY
    answer()

def board_fct():
    global board
    while True:
        line = input()
        if line == "DONE":
            break
        values = line.split(',')
        board[int(values[1])][int(values[0])] = int(values[2])
    answer()

def info(cmd):
    pass

def about():
    print("name=\"bigbrain\", version=\"1.0\", author=\"antoine\", country=\"France\"", flush=True)

command_functions = {
    "END": sys.exit,
    "START": start,
    "ABOUT": about,
    "BEGIN": begin,
    "TURN": turn,
    "BOARD": board_fct,
    "INFO": info
}

def exec_cmd(cmd):
    global Start, board
    splited_cmd = cmd.split(' ')
    command = splited_cmd[0]

    if command in command_functions:
        command_functions[command](*splited_cmd[1:])
    else:
        print("ERROR - unknown command", flush=True)

def main():
    while True:
        line = input()
        exec_cmd(line)

if __name__ == '__main__':
    main()

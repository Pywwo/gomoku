#!/usr/bin/env python3

import sys
import tree_minmax

Start = False
ENNEMY = 2
ME = 1
board = 0

def start(size):
    global Start, board
    if size < 5 or size > 20:
        print ("ERROR unsupported size", flush=True)
    else:
        Start = True
        board = []
        for i in range(size):
            board.append([0] * size)
        print ("OK", flush=True)

def answer():
    global board

    tmp_tree = tree_minmax.Tree(1, 2, board)
    to_play = tmp_tree.get_minmax_score()
    board[to_play[1]][to_play[2]] = 1
    print ("{},{}".format(to_play[2], to_play[1]), flush=True)

def begin():
    global board
    answer()
    return

def turn(x, y):
    global board
    board[y][x] = ENNEMY
    answer()
    return

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
    return

def about():
    print ("name=\"bigbrain\", version=\"1.0\", author=\"antoine\", country=\"France\"", flush=True)

def exec_cmd(cmd):
    global Start, board
    splitedCmd = cmd.split(' ')
    if splitedCmd[0] == "END":
        sys.exit(0)
    elif splitedCmd[0] == "START":
        start(int(splitedCmd[1]))
        return
    elif splitedCmd[0] == "ABOUT":
        about()
        return
    elif splitedCmd[0] == "BEGIN":
        begin()
        return
    elif splitedCmd[0] == "TURN":
        pos = splitedCmd[1].split(',')
        turn(int(pos[0]), int(pos[1]))
        return
    elif splitedCmd[0] == "BOARD":
        board_fct()
        return
    elif splitedCmd[0] == "INFO":
        info(cmd)
        return
    else:
        print ("ERROR - unknown command", flush=True)

def main():
    while True:
        line = input()
        exec_cmd(line)

if __name__=='__main__':
    main()

"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

    return [[X, EMPTY, EMPTY],
            [O, O, EMPTY],
            [X, O, X]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board != initial_state():
        return X
    
    board_xs = 0
    board_os = 0

    for row in board:
        for spot in row:
            if spot == O:
                board_os += 1
            elif spot == X:
                board_xs += 1

    if board_xs > board_os:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    irow = 0
    icol = 0
    for row in board:
        for spot in row:
            if spot == EMPTY:
                moves.add((irow, icol))
                icol += 1
            else:
                icol += 1
                continue
        icol = 0
        irow += 1
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")

    next = player(board)
    new_play = copy.deepcopy(board)
    new_play[action[0]][action[1]] = next
    return new_play

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

start = initial_state()
result(start, (0, 1))
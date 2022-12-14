"""
Tic Tac Toe Player
"""

from cmath import inf
import math
import copy
import random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_o = 0
    count_x = 0
    for row in board:
        count_o += row.count(O)
        count_x += row.count(X)
    
    if count_x == count_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    
    for row in [0,1,2]:
        for col in [0,1,2]:
            if board[row][col] == EMPTY:
                actions.append((row, col))
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    else:
        raise Exception("Invalid action")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        row_result = ''.join(str(row))
        if row_result == 'XXX':
            return X
        elif row_result == 'OOO':
            return O
    
    for col in list(map(list, zip(*board))):
        col_result = ''.join(str(col))
        if col_result == 'XXX':
            return X
        elif col_result == 'OOO':
            return O

    diag1_result = ''.join([str(board[i][i]) for i in range(3)])
    if diag1_result == 'XXX':
        return X
    elif diag1_result == 'OOO':
        return O

    diag2_result = ''.join([str(board[i][2-i]) for i in range(3)])
    if diag2_result == 'XXX':
        return X
    elif diag2_result == 'OOO':
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        count_empty = 0
        for row in board:
            count_empty += row.count(EMPTY)
        
        if count_empty == 0:
            return True
        else:
            return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _, minimax_action = max_value(board)
    else:
        _, minimax_action = min_value(board)
    
    return minimax_action

def min_value(board):
    print(terminal(board))
    if terminal(board):
        return utility(board), None
    v = float('inf')
    minimax_action = None
    for action in actions(board):
        max_v, _ = max_value(result(board, action))
        if max_v < v:
            minimax_action = action
            v = max_v
            if v == -1:
                return v, minimax_action
    
    return v, minimax_action


def max_value(board):
    print(terminal(board))
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    minimax_action = None
    for action in actions(board):
        min_v, _ = min_value(result(board, action))
        if min_v > v:
            minimax_action = action
            v = min_v
            if v == 1:
                return v, minimax_action

    return v, minimax_action    

           






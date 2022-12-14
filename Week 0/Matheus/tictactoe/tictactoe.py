"""
Tic Tac Toe Player
"""

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

    # return [[X, EMPTY, X],
    #         [X, O, X],
    #         [O, X, O]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    start_config = initial_state()
    if board == start_config:
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
    if len(moves) == 0:
        raise Exception("No moves available")
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

    "Checks rows"
    for row in board:
        if all(x == row[0] for x in row): # The all() function returns True if all items in an iterable are true, otherwise it returns False
            if row[0] == X:
                xwin = True
                return X
            elif row[0] == O:
                owin = True
                return O
    
    "Checks columns"
    for column in range(3):
        x = []
        for row in range(3):
            x.append(board[row][column])

        if all(spot == x[0] for spot in x):
            if x[0] == X:
                xwin = True
                return X
            elif x[0] == O:
                owin = True
                return O

    "Checks diagonals"
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if all(x == diagonal1[0] for x in diagonal1):
        if board[0][0] == X:
            xwin = True
            return X
        elif board[0][0] == O:
            owin = True
            return O
    elif all(x == diagonal2[0] for x in diagonal2):
        if board[0][2] == X:
            xwin = True
            return X
        elif board[0][2] == O:
            owin = True
            return O

    return None # No winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    elif all(spot != EMPTY for row in board for spot in row):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # moves = list(actions(board))
    # num_moves = len(moves)
    # a = random.randint(0,num_moves-1)
    # return moves[a]

    if terminal(board):
        return None
    else:
        if player(board) == X:
            _, move = max(board)
            return move
        else:
            _, move = min(board)
            return move


def max(board):
    if terminal(board):
        return utility(board), None

    cost = float('-inf')
    move = None
    for action in actions(board):
        current, _ = min(result(board, action))
        if current > cost:
            cost = current
            move = action
            if cost == 1:
                return cost, move

    return cost, move

def min(board):
    if terminal(board):
        return utility(board), None

    cost = float('inf')
    move = None
    for action in actions(board):
        current, _ = max(result(board, action))
        if current < cost:
            cost = current
            move = action
            if cost == -1:
                return cost, move

    return cost, move
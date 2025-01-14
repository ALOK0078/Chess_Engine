import chess

def create_board():
    return chess.Board()

def make_move(board, move):
    board.push(move)

def undo_move(board):
    board.pop()

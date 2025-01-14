import chess
from core.evaluation import evaluate_board

def test_king_safety():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert evaluate_board(board) == 0, "King safety should be neutral in the starting position"

    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQ1BNR w KQkq - 0 1")  # White king exposed
    assert evaluate_board(board) < 0, "White king safety should be penalized"

def test_center_control():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1")
    assert evaluate_board(board) > 0, "White should have better center control with e4 played"

from core.board import create_board
from core.search import minimax
from core.evaluation import evaluate_board
import chess
if __name__ == "__main__":
    board = create_board()

    print("Initial Board:")
    print(board)
    manual_move = "c2c4"  # Replace with the desired move in UCI format
    move = chess.Move.from_uci(manual_move)
    if move in board.legal_moves:
        # Get the SAN notation BEFORE pushing the move
        move_san = board.san(move)
        board.push(move)
        print(f"\nManual Move Played:  {move_san}")
        print("\nBoard After Manual Move:")
        print(board)
    else:
        print(f"Illegal move: {manual_move}")
        exit()
    depth = 2  # Depth of the Minimax search
    print("\nThinking...")
    _, best_move = minimax(board, depth, float('-inf'), float('inf'), True)

    if best_move:
        print(f"\nBest Move: {board.san(best_move)}")
        board.push(best_move)
        print("\nBoard After Best Move:")
        print(board)
        print("Evaluation:", evaluate_board(board))
    else:
        print("No legal moves available.")

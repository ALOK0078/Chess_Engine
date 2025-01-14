import chess
from core.evaluation import evaluate_board


def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Minimax algorithm with alpha-beta pruning.
    Args:
        board (chess.Board): The current board state.
        depth (int): Depth of the search tree.
        alpha (float): Alpha value for pruning.
        beta (float): Beta value for pruning.
        maximizing_player (bool): True if maximizing, False if minimizing.

    Returns:
        float: Evaluation score of the best move.
        chess.Move: The best move at the current depth.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None  # Return evaluation of the current board

    best_move = None

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval, best_move

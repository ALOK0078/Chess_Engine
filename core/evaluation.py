import chess
from core.tables import PAWN_TABLE, KNIGHT_TABLE, BISHOP_TABLE, ROOK_TABLE, QUEEN_TABLE, KING_TABLE

def evaluate_board(board):
    material_scores = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 0
    }

    positional_scores = {
        chess.PAWN: PAWN_TABLE,
        chess.KNIGHT: KNIGHT_TABLE,
        chess.BISHOP: BISHOP_TABLE,
        chess.ROOK: ROOK_TABLE,
        chess.QUEEN: QUEEN_TABLE,
        chess.KING: KING_TABLE
    }

    score = 0

    # Evaluate White's pieces
    for piece_type in material_scores:
        for square in board.pieces(piece_type, chess.WHITE):
            score += material_scores[piece_type]
            if piece_type in positional_scores:
                score += positional_scores[piece_type][square]

    # Evaluate Black's pieces (reverse positional scores for Black)
    for piece_type in material_scores:
        for square in board.pieces(piece_type, chess.BLACK):
            score -= material_scores[piece_type]
            if piece_type in positional_scores:
                score -= positional_scores[piece_type][chess.square_mirror(square)]

    return score
def evaluate_king_safety(board):
    """
    Evaluates the safety of kings.
    Penalizes exposed kings and rewards good pawn shielding.
    """
    king_safety_score = 0

    # Evaluate White king safety
    white_king_square = board.king(chess.WHITE)
    white_pawns_near_king = sum(1 for sq in chess.SquareSet(chess.BB_KING_ATTACKS[white_king_square])
                                if board.piece_at(sq) == chess.Piece(chess.PAWN, chess.WHITE))
    if white_pawns_near_king < 2:
        king_safety_score -= 50  # Penalize for lack of pawn shielding

    # Evaluate Black king safety
    black_king_square = board.king(chess.BLACK)
    black_pawns_near_king = sum(1 for sq in chess.SquareSet(chess.BB_KING_ATTACKS[black_king_square])
                                if board.piece_at(sq) == chess.Piece(chess.PAWN, chess.BLACK))
    if black_pawns_near_king < 2:
        king_safety_score += 50  # Penalize for lack of pawn shielding

    return king_safety_score

def evaluate_mobility(board):
    """
    Evaluates the mobility of pieces.
    Rewards having more legal moves.
    """
    mobility_score = 0
    mobility_score += len(list(board.legal_moves)) * 10  # Reward mobility
    return mobility_score

def evaluate_center_control(board):
    """
    Evaluates control of the center (squares d4, e4, d5, e5).
    Rewards pieces occupying or attacking these squares.
    """
    center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    center_control_score = 0

    for square in center_squares:
        if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
            center_control_score += 20
        elif board.piece_at(square) and board.piece_at(square).color == chess.BLACK:
            center_control_score -= 20

    return center_control_score
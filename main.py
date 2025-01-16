from core.board import create_board
from core.search import minimax
from core.evaluation import evaluate_board
import chess

def get_player_move(board):
    """Prompts the player for a move and validates it."""
    while True:
        user_move = input("Your move (e.g., e2e4): ")
        try:
            move = chess.Move.from_uci(user_move)
            if move in board.legal_moves:
                return move
            else:
                print("Illegal move. Try again.")
        except:
            print("Invalid format. Please use UCI format (e.g., e2e4).")

def print_evaluation_bar(score):
    """Displays an evaluation bar based on the evaluation score."""
    max_bar_length = 20  # Length of the bar
    normalized_score = max(min(score, 1000), -1000)  # Limit score between -1000 and 1000
    bar_position = int((normalized_score + 1000) / 2000 * max_bar_length)

    bar = "|" * bar_position + "-" * (max_bar_length - bar_position)
    
    if score > 0:
        advantage = "White is better"
    elif score < 0:
        advantage = "Black is better"
    else:
        advantage = "Equal position"

    print(f"\nEvaluation Bar: [{bar}] {score}")
    print(f"Advantage: {advantage}\n")

def play_game():
    """Runs the player vs. engine game loop."""
    board = create_board()
    depth = 3  # Depth of the engine search

    print("Welcome to the Chess Engine!")
    print(board)

    while not board.is_game_over():
        # Player's Turn
        player_move = get_player_move(board)
        board.push(player_move)
        print("\nPlayer's Move:")
        print(board)

        # Show evaluation after the player's move
        score = evaluate_board(board)
        print_evaluation_bar(score)

        if board.is_game_over():
            break

        # Engine's Turn
        print("\nEngine is thinking...")
        _, engine_move = minimax(board, depth, float('-inf'), float('inf'), True)

        if engine_move and engine_move in board.legal_moves:
            move_san = board.san(engine_move)  # Convert to SAN before pushing
            board.push(engine_move)
            print(f"\nEngine plays: {move_san}")
            print(board)

            # Show evaluation after the engine's move
            score = evaluate_board(board)
            print_evaluation_bar(score)
        else:
            print("Engine could not find a legal move. Game over.")
            break

    # Game Over
    print("\nGame Over!")
    result = board.result()
    if result == '1-0':
        print("White wins!")
    elif result == '0-1':
        print("Black wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()


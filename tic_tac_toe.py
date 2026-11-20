"""A two-player console Tic Tac Toe game. Run with Python 3.10+."""

WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def display_board(board):
    """Return a readable board, showing numbers for available squares."""
    cells = [cell or str(i + 1) for i, cell in enumerate(board)]
    return "\n---+---+---\n".join(
        " " + " | ".join(cells[i:i + 3]) for i in range(0, 9, 3)
    )


def winner(board):
    """Return the winning mark, or None if neither player has won."""
    for a, b, c in WINNING_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def make_move(board, choice, player):
    """Place a mark; invalid input leaves the board unchanged."""
    try:
        square = int(choice)
    except ValueError:
        raise ValueError("Enter a whole number from 1 to 9.") from None
    if not 1 <= square <= 9:
        raise ValueError("Choose a square from 1 to 9.")
    if board[square - 1]:
        raise ValueError("That square is taken. Choose an empty square.")
    if player not in ("X", "O"):
        raise ValueError("Player must be X or O.")
    board[square - 1] = player


def play_game():
    board = [""] * 9
    player = "X"
    while True:
        print("\n" + display_board(board))
        choice = input(f"Player {player}, choose a square (1-9), or q to quit: ").strip()
        if choice.lower() == "q":
            return False
        try:
            make_move(board, choice, player)
        except ValueError as error:
            print(error)
            continue
        result = winner(board)
        if result or all(board):
            print("\n" + display_board(board))
            print(f"Player {result} wins!" if result else "It's a draw!")
            return True
        player = "O" if player == "X" else "X"


def main():
    print("Tic Tac Toe - two players, one keyboard. X goes first.")
    try:
        while play_game():
            if input("Play again? (y/n): ").strip().lower() != "y":
                break
    except (EOFError, KeyboardInterrupt):
        print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()

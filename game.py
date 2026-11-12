BOARD_SIZE = 3
EMPTY = " "
MARKS = ("X", "O")
TOTAL_CELLS = BOARD_SIZE * BOARD_SIZE


def is_win(game):
    """Return True if X or O has three-in-a-row.

    Args:
        game: A BOARD_SIZE x BOARD_SIZE board. Each cell is " ", "X", or "O".

    Returns:
        True when one row, column, or diagonal is all X or all O.
    """
    lines = []
    for i in range(BOARD_SIZE):
        lines.append([(i, j) for j in range(BOARD_SIZE)])
        lines.append([(j, i) for j in range(BOARD_SIZE)])
    lines.append([(i, i) for i in range(BOARD_SIZE)])
    lines.append([(i, BOARD_SIZE - 1 - i) for i in range(BOARD_SIZE)])

    for cells in lines:
        values = [game[r][c] for r, c in cells]
        if values[0] in MARKS and all(value == values[0] for value in values):
            return True
    return False


def read_move(game):
    """Read a 1-based cell and return 0-based (row, column).

    Args:
        game: Current board, used to reject occupied cells.

    Returns:
        A tuple (row, column) with indexes in 0 .. BOARD_SIZE-1.
    """
    while True:
        try:
            raw = input(
                f"Which cell to mark? i:[1..{BOARD_SIZE}], j:[1..{BOARD_SIZE}]: "
            )
            i, j = map(int, raw.split())
        except ValueError:
            print("Please enter two integers, e.g. 1 2")
            continue

        if not (1 <= i <= BOARD_SIZE and 1 <= j <= BOARD_SIZE):
            print(f"Coordinates must be between 1 and {BOARD_SIZE}.")
            continue

        i -= 1
        j -= 1
        if game[i][j] != EMPTY:
            print("That cell is already taken. Try again.")
            continue
        return i, j


def is_valid_board(game):
    """Return True if game is a square board of EMPTY, X, and O cells."""
    if len(game) != BOARD_SIZE:
        return False
    for row in game:
        if len(row) != BOARD_SIZE:
            return False
        if any(cell not in (EMPTY,) + MARKS for cell in row):
            return False
    return True


def print_board(game):
    """Print one row of the board per line.

    Args:
        game: A valid tic-tac-toe board.

    Returns:
        None.
    """
    for row in game:
        print(" ".join(row))


def show_board(game, label):
    """Print a label and the board when the board is valid.

    Args:
        game: Board to display.
        label: Heading printed above the grid.

    Returns:
        None.
    """
    if not is_valid_board(game):
        print("Board is invalid and will not be printed.")
        return
    print(label)
    print_board(game)
    print()


def main():
    """Run one two-player tic-tac-toe game on the console."""
    game = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player_marks = {False: "X", True: "O"}  # False = Player 1, True = Player 2
    turn = True  # toggled to False before first move -> Player 1 first
    winner = False

    print("X = Player 1")
    print("O = Player 2")
    show_board(game, "Initial board:")

    for _ in range(TOTAL_CELLS):
        turn = not turn
        player = 1 if turn is False else 2
        print(f"Player {player}: ", end="")

        i, j = read_move(game)
        game[i][j] = player_marks[turn]
        show_board(game, "Current board:")

        if is_win(game):
            print("Win!")
            winner = True
            break

    if not winner:
        print("Tie!")


if __name__ == "__main__":
    main()

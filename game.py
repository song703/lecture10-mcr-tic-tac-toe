def is_win(game):
    """Return True if X or O has three-in-a-row."""
    lines = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for a, b, c in lines:
        va = game[a[0]][a[1]]
        vb = game[b[0]][b[1]]
        vc = game[c[0]][c[1]]
        if va == vb == vc and va in ("X", "O"):
            return True
    return False


def read_move(game):
    """Read a 1-based cell (i, j), convert to 0-based, and validate."""
    while True:
        try:
            raw = input("Which cell to mark? i:[1..3], j:[1..3]: ")
            i, j = map(int, raw.split())
        except ValueError:
            print("Please enter two integers, e.g. 1 2")
            continue

        if not (1 <= i <= 3 and 1 <= j <= 3):
            print("Coordinates must be between 1 and 3.")
            continue

        i -= 1
        j -= 1
        if game[i][j] != " ":
            print("That cell is already taken. Try again.")
            continue
        return i, j


def print_board(game):
    for row in game:
        print(" ".join(row))


def show_board(game, label):
    print(label)
    print_board(game)
    print()


def main():
    game = [[" " for _ in range(3)] for _ in range(3)]
    marks = {False: "X", True: "O"}  # False = Player 1, True = Player 2
    turn = True  # toggled to False before first move -> Player 1 first
    winner = False

    print("X = Player 1")
    print("O = Player 2")
    show_board(game, "Initial board:")

    for n in range(9):
        turn = not turn
        player = 1 if turn is False else 2
        print(f"Player {player}: ", end="")

        i, j = read_move(game)
        game[i][j] = marks[turn]
        show_board(game, "Current board:")

        if is_win(game):
            print("Win!")
            winner = True
            break

    if not winner:
        print("Tie!")


if __name__ == "__main__":
    main()

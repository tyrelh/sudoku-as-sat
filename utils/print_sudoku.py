def print_board(board: list):
    """Prints a sudoku board from a 2d list.

    Args:
        board: 2D list [y][x] of sudoku board.

    """
    for row in board:
        print(' '.join(str(e) for e in row))

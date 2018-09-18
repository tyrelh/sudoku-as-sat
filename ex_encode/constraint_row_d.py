# from parser import parse
from utils import map_xyz


def gen_constraint_row_d(game: list):
    """Converts 2D list holding game in std format
     to CNF in DIMACS format for row definedness constraint.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the constraint
        in DIMACS form.

    """
    n = len(game)
    dimacs = []
    for r in range(1, n + 1): # AND
        for v in range(1, n + 1): # AND
            literals = []
            for c in range(1, n + 1): # OR
                literals.append(map_xyz.map_ijk_to_num(r, c, v, n))
            clause = ' '.join(str(literal) for literal in literals)
            dimacs.append('{} 0'.format(clause)) 
    return '\n'.join(dimacs)


if __name__ == '__main__':
    """Tests for constraint: row definedness.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(gen_constraint_row_d(game))
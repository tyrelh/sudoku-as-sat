# from parser import parse
from utils import map_xyz


def gen_constraint_cell_u(game: list):
    """Converts 2D list holding game in std format
     to CNF in DIMACS format for cell uniqueness constraint.

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
        for c in range(1, n + 1): # AND
            for vi in range (1, n): # AND
                for vj in range (vi + 1, n + 1): # AND
                    literals = [
                        -map_xyz.map_ijk_to_num(r, c, vi, n),
                        -map_xyz.map_ijk_to_num(r, c, vj, n),
                    ]
                    clause = ' '.join(str(literal) for literal in literals)
                    dimacs.append('{} 0'.format(clause))
    return '\n'.join(dimacs)


if __name__ == '__main__':
    """Testsfor constraint: cell uniqueness.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[0]
    print(gen_constraint_cell_u(game))
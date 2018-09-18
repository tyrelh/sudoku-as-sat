# from parser import parse
from utils import map_xyz


def gen_constraint_col_u(game: list):
    """Converts 2D list holding game in std format
     to CNF in DIMACS format for col uniqueness constraint.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the constraint
        in DIMACS form.

    """
    n = len(game)
    dimacs = []
    for c in range(1, n + 1): # AND
        for v in range(1, n + 1): # AND
            for ri in range(1, n): # AND
                for rj in range(ri + 1, n + 1): # AND
                    literals = [
                        -map_xyz.map_ijk_to_num(ri, c, v, n),
                        -map_xyz.map_ijk_to_num(rj, c, v, n),
                    ]
                    clause = ' '.join(str(literal) for literal in literals)
                    dimacs.append('{} 0'.format(clause))
    return '\n'.join(dimacs)


if __name__ == '__main__':
    """Tests for constraint: col uniqueness.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(gen_constraint_col_u(game))
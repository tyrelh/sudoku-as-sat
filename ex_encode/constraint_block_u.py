# from parser import parse
from utils import map_xyz
import math


def gen_constraint_block_u(game: list):
    """Converts 2D list holding game in std format
     to CNF in DIMACS format for block uniqueness constraint.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the constraint
        in DIMACS form.

    """
    n = len(game)
    sqrt_n = int(math.sqrt(n))
    dimacs = []
    for r_offs in range(0, sqrt_n): # AND   CHANGED RANGE FROM PAPER!
        for c_offs in range(0, sqrt_n): # AND   CHANGED RANGE FROM PAPER!
            for v in range(1, n + 1): # AND
                for r in range(1, sqrt_n + 1): # AND
                    for c in range(r + 1, sqrt_n + 1): # AND
                        literals = []
                        r_val_1 = r_offs * sqrt_n + (r )#% sqrt_n)
                        c_val_1 = c_offs * sqrt_n + (r )#% sqrt_n)
                        r_val_2 = r_offs * sqrt_n + (c )#% sqrt_n)
                        c_val_2 = c_offs * sqrt_n + (c )#% sqrt_n)
                        literals.append(-map_xyz.map_ijk_to_num(r_val_1, c_val_1, v, n))
                        literals.append(-map_xyz.map_ijk_to_num(r_val_2, c_val_2, v, n))
                        clause = ' '.join(str(literal) for literal in literals)
                        dimacs.append('{} 0'.format(clause))
    return '\n'.join(dimacs)


if __name__ == '__main__':
    """Tests for constraint: block uniqueness.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(gen_constraint_block_u(game))
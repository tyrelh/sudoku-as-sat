# from parser import parse
from utils import map_xyz
import math


def gen_constraint_block_d(game: list):
    """Converts 2D list holding game in std format
     to CNF in DIMACS format for block definedness constraint.

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
    for r_offs in range(0, sqrt_n): # AND  was range(1, sqrt_n + 1)
        for c_offs in range(0, sqrt_n): # AND was range(1, sqrt_n + 1)
            for v in range (1, n + 1): # AND
                literals = []
                for r in range(1, sqrt_n + 1): # OR
                    for c in range(1, sqrt_n + 1): # OR
                        r_val = r_offs * sqrt_n + r
                        c_val = c_offs * sqrt_n + c
                        literals.append(map_xyz.map_ijk_to_num(r_val, c_val, v, n))
                clause = ' '.join(str(literal) for literal in literals)
                dimacs.append('{} 0'.format(clause))

    return '\n'.join(dimacs)


if __name__ == '__main__':
    """Tests for constraint: block definedness.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(gen_constraint_block_d(game))
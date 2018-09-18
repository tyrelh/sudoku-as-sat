from sud2sat.parser import parse

import math

from utils import map_xyz


def gen_constraint_4(game: list):
    """Converts 2D list holding game in std format
     to CNF in DMax format for constraint 4.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the game
        in DIMACS form.

    """

    n = len(game)
    n_root = int(math.sqrt(n))
    dmax_list_1 = []
    dmax_list_2 = []
    for z in range(1, n + 1):
        for i in range(0, n_root):
            for j in range(0, n_root):
                for x in range(1, n_root + 1):
                    for y in range(1, n_root + 1):
                        for k in range(y + 1, n_root + 1):
                            a = map_xyz.map_ijk_to_num(n_root * i + x, n_root * j + y, z, n)
                            b = map_xyz.map_ijk_to_num(n_root * i + x, n_root * j + k, z, n)
                            dmax_list_1.append('-{} -{} 0'.format(a, b))
    for z in range(1, n + 1):
        for i in range(0, n_root):
            for j in range(0, n_root):
                for x in range(1, n_root):
                    for y in range(1, n_root + 1):
                        for k in range(x + 1, n_root + 1):
                            for l in range(1, n_root + 1):
                                a = map_xyz.map_ijk_to_num(n_root * i + x, n_root * j + y, z, n)
                                b = map_xyz.map_ijk_to_num(n_root * i + k, n_root * j + l, z, n)
                                dmax_list_2.append('-{} -{} 0'.format(a, b))

    dimacs_string_1 = '\n'.join(dmax_list_1)
    dimacs_string_2 = '\n'.join(dmax_list_2)
    return dimacs_string_1 + '\n' + dimacs_string_2


if __name__ == '__main__':
    """Tests for gen_constraint_4.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[0]
    dimacsForm = gen_constraint_4(game)
    print(dimacsForm)
    debug = dimacsForm.split('\n')
    print("Length: " + str(len(debug)))

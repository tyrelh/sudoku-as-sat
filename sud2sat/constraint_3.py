from sud2sat.parser import parse

from utils import map_xyz


def gen_constraint_3(game: list):
    """Converts 2D list holding game in std format
     to CNF in DMax format for constraint 3.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the game
        in DIMACS form.

    """
    n = len(game)
    dmax_list = []
    for x in range(1, n + 1):
        for z in range(1, n + 1):
            for y in range(1, n):
                for i in range(y + 1, n + 1):
                    row = [
                        -map_xyz.map_ijk_to_num(x, y, z, n),
                        -map_xyz.map_ijk_to_num(x, i, z, n),
                    ]
                    line = ' '.join(str(e) for e in row)
                    dmax_list.append('{} 0'.format(line))
    return '\n'.join(dmax_list)


if __name__ == '__main__':
    """Tests for non_empty_boolean method.
    """
    path = '../data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(gen_constraint_3(game))

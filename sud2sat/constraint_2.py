from utils import map_xyz


def gen_constraint_2(game: list):
    """Converts 2D list holding game in std format
     to CNF in DMax format for constraint 2.

    Args:
        game (list): A 2D array of ints representing
        the start state of a sudoku game.

    Returns:
        str: A string representing the CNF of the game
        in DIMACS form.

    """

    n = len(game)
    dmax_list = []
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            for x in range(1, n):
                for i in range(x + 1, n + 1):
                    row = [
                        -map_xyz.map_ijk_to_num(x, y, z, n),
                        -map_xyz.map_ijk_to_num(i, y, z, n),
                    ]
                    line = ' '.join(str(e) for e in row)
                    dmax_list.append('{} 0'.format(line))
    return '\n'.join(dmax_list)


if __name__ == '__main__':
    """Tests for gamestate_to_dimacs_constraint_2.
    """
    # path = '../data/p096_sudoku.txt'
    # grids = parse(path)
    # game = grids[1]
    game = [
        [1, 3, 0],
        [2, 0, 0],
        [0, 1, 0]
    ]
    # for line in game:
    #     print(str(line))
    dmaxForm = gen_constraint_2(game)
    print(dmaxForm)

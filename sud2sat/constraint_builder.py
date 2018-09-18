from sud2sat.constraint_1 import gen_constraint_1
from sud2sat.constraint_2 import gen_constraint_2
from sud2sat.constraint_3 import gen_constraint_3
from sud2sat.constraint_4 import gen_constraint_4
from sud2sat.parser import parse
from utils import map_xyz
import sys


def set_known_values(game):
    dimacs_list = []
    n = len(game)
    for x in range(n):
        for y in range(n):
            z = game[y][x]
            if z > 0:
                dimacs_list.append('{} 0'.format(map_xyz.map_ijk_to_num(x+1, y+1, z, n)))
    return '\n'.join(dimacs_list)


def build_constraint(game):
    val = pow(len(game), 3)
    constraint = ''
    constraint += '{}\n'.format(gen_constraint_1(game))
    constraint += '{}\n'.format(gen_constraint_2(game))
    constraint += '{}\n'.format(gen_constraint_3(game))
    constraint += '{}\n'.format(gen_constraint_4(game))
    constraint += '{}'.format(set_known_values(game))
    header = 'p cnf {} {}\n'.format((len(game)**3), len(constraint.split('\n')))

    return header + constraint


if __name__ == '__main__':
    """Tests for non_empty_boolean method.
    """

    if len(sys.argv) < 2:
        print("No puzzle format argument!!!")

    puzzle_format = sys.argv[1]

#    puzzle_format = 'r'
    path = './data/p096_sudoku.txt'
    grids = parse(path, puzzle_format)
    game = grids[1]
    print(build_constraint(game))

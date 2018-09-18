from ex_encode.constraint_cell_d import gen_constraint_cell_d
from ex_encode.constraint_cell_u import gen_constraint_cell_u
from ex_encode.constraint_row_d import gen_constraint_row_d
from ex_encode.constraint_row_u import gen_constraint_row_u
from ex_encode.constraint_col_d import gen_constraint_col_d
from ex_encode.constraint_col_u import gen_constraint_col_u
from ex_encode.constraint_block_d import gen_constraint_block_d
from ex_encode.constraint_block_u import gen_constraint_block_u


# from parser import parse
from utils import map_xyz


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
    constraint = ''
    constraint += '{}\n'.format(gen_constraint_cell_d(game))
    constraint += '{}\n'.format(gen_constraint_cell_u(game))
    constraint += '{}\n'.format(gen_constraint_row_d(game))
    constraint += '{}\n'.format(gen_constraint_row_u(game))
    constraint += '{}\n'.format(gen_constraint_col_d(game))
    constraint += '{}\n'.format(gen_constraint_col_u(game))
    constraint += '{}\n'.format(gen_constraint_block_d(game))
    constraint += '{}\n'.format(gen_constraint_block_u(game))
    constraint += '{}'.format(set_known_values(game))
    header = 'p cnf 729 {}\n'.format(len(constraint.split('\n')))

    return header + constraint


if __name__ == '__main__':
    """Tests for non_empty_boolean method.
    """
    path = './data/p096_sudoku.txt'
    grids = parse(path)
    game = grids[1]
    print(build_constraint(game))

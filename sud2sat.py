import sys

from ex_encode import constraint_builder as ex_encode_builder
from sud2sat import constraint_builder as sud2sat_builder
from sud2sat.parser import parse


def run_file(path, input_type, encoding):
    grids = parse(path, input_type)
    game_num = 0
    for game in grids:
        game_num += 1

        # Build constraints and print them.
        if encoding:
            print(ex_encode_builder.build_constraint(game))
        else:
            print(sud2sat_builder.build_constraint(game))


if __name__ == '__main__':
    encoding = None
    if len(sys.argv) > 3:
        encoding = sys.argv[3]
    path = sys.argv[1]
    run_file(path, sys.argv[2], encoding)

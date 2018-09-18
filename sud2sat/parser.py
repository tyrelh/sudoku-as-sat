#!/usr/bin/python3
import math
import string


ch_to_int = {v: k for k, v in enumerate(string.digits + string.ascii_letters)}


def parse(filename: str, input_format):
    """ Parses input 'filename' to form a list, 'grids', of individual games

    :param filename: name of input file containing one or more games
    :param input_format: format of file data; 'g' game on each line, 'r' game row on each line
    :return: 'grids' the list of input games
    """


    grids = []
    with open(filename) as f:

        line = f.readline()
        row = []
        while line:
            if 'Grid' in line:
                line = f.readline()
            row = replace_blanks(line)
            n = len(row) if input_format is 'r' else int(math.sqrt(len(row)))
            cur_grid = []
            if input_format is 'g':
                for i in range(n):
                    cur_grid.append(row[(i*n):(i*n+n)])
            else:
                cur_grid.append(row)
                for j in range(n-1):
                    line = f.readline()
                    row = replace_blanks(line)
                    cur_grid.append(row)
            grids.append(cur_grid)
            line = f.readline()
    return grids


def replace_blanks(line: str):
    null_vals = ['.', '*', '?']
    new_row = []
    for x in line.strip():
        if x in null_vals:
            x = '0'
        new_row.append(int(ch_to_int[x]))
    return new_row


if __name__ == '__main__':
    """Tests the parse method."""
    path = '../data/hard_games.txt'
    grids = parse(path, 'r')
    for i, grid in enumerate(grids):
        print('\nGrid {}'.format(i))
        for row in grid:
            print(' '.join(str(e) for e in row))

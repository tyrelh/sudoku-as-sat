from utils import map_xyz
from utils import print_sudoku


def parse_ouput_file(path: str):
    """Parses a miniSat output.txt file.

    Args:
        path: Path to `output.txt`

    Returns:
        list: 2D list [y][x] of sudoku board.

    """
    values = {}
    with open(path) as f:
        raw =  f.readlines()
        if 'UNSAT' in raw[0]:
            print ("ERROR: Input is unsatisfiable.")
            exit(0)
        output =raw[1]
        num_list = [int(s) for s in output.strip().split(' ')]
        for e in num_list[:-1]:
            # print(e)
            if e <= 0:
                continue
            i, j, k = map_xyz.map_num_to_ijk(e, 9)
            values[(i, j,)] = k

    output = []
    for y in range(1, 9 + 1):
        temp_y = []
        for x in range(1, 9 + 1):
            z = values.get((x, y,), -1)
            temp_y.append(z)
        output.append(temp_y)
    return output


if __name__ == '__main__':
    path = '../sud2sat/output.txt'
    # board = parse_ouput_file(path)
    board = sat2sud(path)
    print_sudoku.print_board(board)

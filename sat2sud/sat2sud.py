import sys, string
from utils import map_xyz


# Takes the output (a 1D representation of a 3D list) from the sat solver and formats it into a printable sudoku puzzle.
def sat_2_sud(line):  # in_from_sat: list
    line[0].strip(' \n\t\n\r')  # May not be necessary but just in case.
    if 'UNSAT' in line[0]:
        print("Unsatisfied")
        return

    in_from_sat = list(map(int, line[1].split()))
    sud_size = int((len(in_from_sat)) ** (1.0 / 3.0))  # cubed root of list size for a side of puzzle (puzzle is nxn)
    num_cells = sud_size * sud_size
    output = [[None for j in range(sud_size)] for i in range(sud_size)]
    for val in in_from_sat:
        if val > 0:
            i, j, k = map_xyz.map_num_to_ijk(val, sud_size)
            output[i - 1][j - 1] = k

    print_puzzle(output, sud_size)


# Prints the 2d representation of the puzzle from a 1D list
def print_puzzle(input_2_print: list, n):
    int_to_ch = string.digits + string.ascii_letters
    for j in range(n):
        for i in range(n):
            print(int_to_ch[int(input_2_print[i][j])], end=" ")
        print()


if __name__ == '__main__':
    line = sys.stdin.readlines()
    sat_2_sud(line)

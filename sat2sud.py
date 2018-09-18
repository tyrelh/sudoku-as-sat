import sys

from sat2sud.sat2sud import sat_2_sud


def run_file(path):
    with open(path) as f:
        minisat_output = f.readlines()
        sat_2_sud(minisat_output)


if __name__ == '__main__':
    path = sys.argv[1]
    run_file(path)

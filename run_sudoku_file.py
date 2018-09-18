import statistics
import subprocess

import sys

from sud2sat import constraint_builder as sud2sat_builder
from ex_encode import constraint_builder as ex_encode_builder
from sat2sud.sat2sud import sat_2_sud

from sud2sat.parser import parse


def run_file(path, input_type, encoding):
    # Ensure that `output.txt` and `input.txt` exist.
    subprocess.run(
        ['touch', 'output.txt', 'input.txt']
    )

    grids = parse(path, input_type)
    game_num = 0
    times = []
    for game in grids:
        game_num += 1

        # Build constraints and write them to `input.txt`.
        if encoding:
            constraint = ex_encode_builder.build_constraint(game)
        else: 
            constraint = sud2sat_builder.build_constraint(game)
        with open('input.txt', 'w') as f:
            f.write(constraint)

        # Run minisat on `input.txt`.
        minisat_stats = subprocess.run(
            ['minisat', 'input.txt', 'output.txt'],
            stdout=subprocess.PIPE,
        ).stdout.decode("utf-8")
        # print(minisat_stats)
        time = -1
        for line in minisat_stats.split('\n'):
            if 'CPU time' in line:
                time = float(line.split(' ')[-2])
                times.append(time)

        # Run `sat2sud` on minisat output.

        with open('output.txt') as f:
            minisat_output = f.readlines()
            print('Game {}'.format(game_num))
            sat_2_sud(minisat_output)
            print('Time {}\n'.format(time))

    print('Times: {}\n'.format(times))
    print('Mean CPU Time: {}'.format(statistics.mean(times)))
    print('Standard Deviation CPU Time: {}'.format(statistics.stdev(times)))
    print('Variance CPU Time: {}'.format(statistics.variance(times)))
    print('Min CPU Time: {}, Game {}'.format(min(times), times.index(min(times))))
    print('Max CPU Time: {}, Game {}'.format(max(times), times.index(max(times))))


if __name__ == '__main__':
    encoding = None
    if len(sys.argv) > 3:
        encoding = sys.argv[3]
    path = sys.argv[1]
    run_file(path, sys.argv[2], encoding)

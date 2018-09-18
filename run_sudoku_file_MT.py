import statistics
import subprocess
import sys

from sud2sat import constraint_builder
from sat2sud.sat2sud import sat_2_sud
from sud2sat.parser import parse

from threading import Thread


def thread_work(game, result, game_num, times):

    # Build constraints and write them to `input.txt`.
    constraint = constraint_builder.build_constraint(game)
    with open('input{}.txt'.format(game_num), 'w') as f:
        f.write(constraint)

    # Run minisat on `input.txt`.
    minisat_stats = subprocess.run(
        ['minisat', 'input{}.txt'.format(game_num), 'output{}.txt'.format(game_num)],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")

    # print(minisat_stats)
    for line in minisat_stats.split('\n'):
        if 'CPU time' in line:
            time = float(line.split(' ')[-2])
            times[game_num] = time


def run_file(path, input_type):
    # Ensure that `output.txt` and `input.txt` exist.
#    subprocess.run(
#        ['touch', 'output.txt', 'input.txt']
#    )

    grids = parse(path, input_type)
    game_num = 0
    num_games = len(grids)
    times = [None] * num_games
    thread = [None] * num_games
    result = [None] * num_games

    for game in grids:

        thread[game_num] = Thread(target=thread_work, args=(game, result, game_num, times))
        thread[game_num].start()
        game_num += 1

    # wait for all threads to finish
    for t in range(num_games):
        thread[t].join()

        # Run `sat2sud` on minisat output.
        with open('output{}.txt'.format(t)) as f:
            minisat_output = f.readlines()
            print('Game {}'.format(t))
            sat_2_sud(minisat_output)
            print('Time {}\n'.format(times[t]))

    print('Times: {}\n'.format(times))
    print('Mean CPU Time: {}'.format(statistics.mean(times)))
    print('Standard Deviation CPU Time: {}'.format(statistics.stdev(times)))
    print('Variance CPU Time: {}'.format(statistics.variance(times)))
    print('Min CPU Time: {}, Game {}'.format(min(times), times.index(min(times))))
    print('Max CPU Time: {}, Game {}'.format(max(times), times.index(max(times))))


if __name__ == '__main__':
    path = sys.argv[1]
    run_file(path, sys.argv[2])

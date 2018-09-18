#!/usr/bin/env bash
set -e

if [ $# -gt 1 ]; then
    export PYTHONPATH=$PYTHONPATH:$PWD
    python3 run_sudoku_file.py $1 $2 $3
else
    echo "usage: run_solver_on_file.sh <your/file/path> <'g' or 'r' puzzle format> <'ex' use extended encoding, optional>"
    echo "'g' for full puzzle on single line, 'r' each line is a row of the puzzle"
    echo "e.g. sh run_solver_on_file.sh g"
fi

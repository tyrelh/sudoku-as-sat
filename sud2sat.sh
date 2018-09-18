#!/usr/bin/env bash
# Generates DIMACS encoding from a sudoku file.

# Expects files to be of the form:
# Title
# encoding
# Title
# encoding
# Title
# encoding
# ...

# Ex:
#   sh ./sud2sat.sh data/input_9x9.txt r > test.txt

set -e

if [ $# -gt 0 ]; then
    export PYTHONPATH=$PYTHONPATH:$PWD
    python3 sud2sat.py $1 $2 $3

else
    echo "Your command line contains no puzzle format arguments"
    echo "'g' for puzzle on single line, 'r' each line is a row of the puzzle"
    echo "e.g. sh run_minisat.sh g"
fi

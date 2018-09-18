#!/usr/bin/env bash
# Generates DIMACS encoding from a sudoku file.

# Expects files to be of the form:
#   SAT
#   -1 -2 3 -4 -5 ...

# Ex:
#   sh ./sat2sud.sh output.txt depr.txt

set -e
export PYTHONPATH=$PYTHONPATH:$PWD
python3 sat2sud.py $1



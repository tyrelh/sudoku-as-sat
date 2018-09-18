# Sudoku as SAT Project

This was a group project built with my friends [@JVerwolf](https://github.com/JVerwolf), [@imagineer6](https://github.com/imagineer6), [@toaplant](https://github.com/toaplant), and [@JeMorriso](https://github.com/JeMorriso) for Foundations of Computer Science (CSC 320) at University of Victoria.

The goal of this project is to encode sudoku games as SAT problems and use
a SAT-solver to find a solution to the game.

There are 3 main steps to the logic of this project. First it will read the
game input and encode the sudoku rules and the initial game state into a
conjunctive normal form (**CNF**) boolean expression in **DIMACS** form. Second, it will
pass this form to the SAT-solver (*miniSAT*) which will try to find a satisfying
solution to the equation and output a solution if one was found. Third we
interpret this output of the SAT-solver back into a solved sudoku game.

*input scripts --> sud2sat --> miniSAT --> sat2sud --> solution!*

This project was written in Python3, and employs a modular directory structure.
To make marking and running the project easy, various shell scripts were
created that solve the tasks outlined in the assignment specification.

### Extended Tasks
Our extended tasks are written into the main logic of our solution. "Hard"
problems as well as n*n problems can be handled by the base logic. Just pass
the games using the syntax outlined below. The "extended encoding" can be used
by passing the -ex flag.


## Running the Project

Running the project end-to-end on a sudoku file:
```
sh ./run_solver_on_file.sh <path> <g|r> <ex>

Args:
    path  Path to a text file containing sudoku game(s).
    g     Each game is on a single line (must use g or r).
    r     Each game is given as a grid (row by row).
    ex    (Optional) use extended encoding.

Examples:
    For the 50 problems from Project Euler:
        ./run_solver_on_file.sh data/p096_sudoku.txt r

    For the 'Hard' problems from magictour:
        ./run_solver_on_file.sh data/hard_games.txt g ex

    For NxN sized boards:
        sh ./run_solver_on_file.sh data/input_9x9.txt r
        sh ./run_solver_on_file.sh data/input_16x16.txt r
        sh ./run_solver_on_file.sh data/input_25x25.txt r
        sh ./run_solver_on_file.sh data/input_36x36.txt r
```
Running sat2sud (minisat output to sudoku board):
```
sh ./sat2sud.sh <path>

Args:
    path  Path to a text file containing miniSat output.

Example:
    sh ./sat2sud.sh minisat_output.txt
```
Running sud2sat (Sudoku file to DIMACS format):
```
sh ./sud2sat.sh <path> <g|r> <ex>

Args:
    path  Path to a text file containing sudoku game(s).
    g     Each game is on a single line (must use g or r).
    r     Each game is given as a grid (row by row).
    ex    (Optional) use extended encoding.

Example:
    sh ./sud2sat.sh data/input_9x9.txt r > test.txt
```

## Directory Structure

data:
* Stores data files containing Sudoku boards.

ex_encode:
* Module for performing the extended encoding.

sat2sud:
* Module for parsing the miniSat output.

sud2sat:
* Module for parsing data files and generating minimal encoding.

utils:
* Common code

app root:
* Python and shell scripts to run application on a given input.

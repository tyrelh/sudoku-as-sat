#!/usr/bin/python
import math, string, random, argparse, sys

def sudoku_maker(N, F, R):
    n = math.sqrt(N)
    s = 0
    o = 1
    g = ""
    d = string.digits + string.ascii_letters
    fill = F

    for l in range(int(N)):
        if l % n == 0:
            s = o
            o += 1
        for __ in range(int(N)):
            r = random.random()
            if r < fill:
                g += d[int(s)]
            else:
                g += '0'
            s = (s % N) + 1
        s = ((s + N - n - 1) % N) + 1
        if l != int(N) - 1:
            if R == False:
                g += "\n"
    return g

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Outputs gameboards')
    parser.add_argument('--size', metavar='N', dest='N', type=int, default=9, help='NxN board (default: %(default)s)')
    parser.add_argument('--games', metavar='G', dest='G', type=int, default=1, help='the number of games (default: %(default)s)')
    parser.add_argument('--fill', metavar='F', dest='F', type=float, default=0.5, help='the square fill rate (default: %(default)s)')
    parser.add_argument('--row', dest='R', type=bool, default=False, help='output on one row (default: %(default)s)')
    args = parser.parse_args()
    o = ""
    for i in range(args.G):
        o += "Grid " + str(i) + "\n"
        o += sudoku_maker(args.N, args.F, args.R)
        o += "\n" if args.G != -1 else ""
    sys.stdout.write(o)

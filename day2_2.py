"""
Day 2, part 2 - Password Philosophy

https://adventofcode.com/2020/day/2

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import re, sys

def main():
    count = 0

    for ele in sys.stdin:
        # print(ele)
        r = re.match("(\d+)-(\d+) (\w): (\w+)", ele).groups()
        Nmin = int(r[0])
        Nmax = int(r[1])
        L = r[2]
        W = r[3]
        if (W[Nmin-1] == L and W[Nmax-1] != L) or (W[Nmin-1] != L and W[Nmax-1] == L):
                count += 1

    print(count)

if __name__ == "__main__":
    main()

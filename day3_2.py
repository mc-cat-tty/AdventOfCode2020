"""
Day 3, part 2 - Toboggan Trajectory

https://adventofcode.com/2020/day/3

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
import math

def main():
    mov_list = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    input_txt = list()
    for line in sys.stdin:
        input_txt.append(line)
    rows_num = len(input_txt)-1  # The last line is blank (EOF or "\n" (?))
    cols_num = sum(1 for char in input_txt[0])-1
    results = list()

    for mov in mov_list:
        count = 0
        (mov_x, mov_y) = mov
        (pos_x, pos_y) = (0, 0)  # Starting position (skipping the first line), keep updated inside the for loop
        
        while pos_x <= rows_num-mov_x:
            (pos_x, pos_y) = (sum(x) for x in zip((pos_x, pos_y), (mov_x, mov_y)))  # Updating current position
            (pos_x, pos_y) = (pos_x, pos_y%cols_num)

            if input_txt[pos_x][pos_y] == "#":
                count += 1
           #     print(input_txt[pos_x][:pos_y]+"X"+input_txt[pos_x][pos_y+1:])
           # else:
           #     print(input_txt[pos_x][:pos_y]+"O"+input_txt[pos_x][pos_y+1:])

        results.append(count)
        print(count, end=' ')

    print(f"\nResult: {math.prod(results)}")


if __name__ == "__main__":
    main()

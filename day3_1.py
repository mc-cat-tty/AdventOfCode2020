"""
Day 3, part 1 - Toboggan Trajectory

https://adventofcode.com/2020/day/3

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys

def main():
    count = 0
    (mov_x, mov_y) = (1, 3)
    (pos_x, pos_y) = (0, 0)  # Starting position, keep updated inside the for loop
    input_txt = list()
    for line in sys.stdin:
        input_txt.append(line)
    cols_num = sum(1 for char in input_txt[0])-1
    
    for line in input_txt[1:]:  # Skip first line
        (pos_x, pos_y) = (sum(x) for x in zip((pos_x, pos_y), (mov_x, mov_y)))  # Updating current position
        (pos_x, pos_y) = (pos_x, pos_y%cols_num)

        if line[pos_y] == "#":
            count += 1
       #     print(line[:pos_y]+"X"+line[pos_y+1:])
       # else:
       #     print(line[:pos_y]+"O"+line[pos_y+1:])


    print(count)


if __name__ == "__main__":
    main()

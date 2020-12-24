"""
Day 6, part 2 - Custom Customs

https://adventofcode.com/2020/day/6

Usage: pipe your input into the script
Keep in mind that you have to add a blank line at the end of the file, otherwise the last group will be ignored
"""

__author__ = "Francesco Mecatti"

import sys
import re

def main():
    ls: List[Set[str]] = list()
    count: int = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:  # Blank line
            count += len(set.intersection(*ls))
            # print(set.intersection(*ls))
            ls = list()
        else:  # Line is an answer that belongs to the current group
            l: List[str] = list(line)
            ls.append(set(l))
    print(count)


if __name__ == "__main__":
    main()

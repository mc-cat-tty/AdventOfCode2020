"""
Day 1, part 1 - Report Repair

https://adventofcode.com/2020/day/1

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys

def main():
    numList = list(sys.stdin)
    for num1 in numList:
        for num2 in numList:
            if int(num1)+int(num2) == 2020:
                print(f"{int(num1)}*{int(num2)} = {int(num1)*int(num2)}")  # first two int conversions are needed in order to strip '\n' character
                return


if __name__ == "__main__":
    main()

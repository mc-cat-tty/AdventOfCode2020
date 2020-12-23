"""
Day 4, part 1 - Passport Processing

https://adventofcode.com/2020/day/4

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
import re

def main():
    count: int = 0
    required_fields: List[str] = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    buf: str = ''
    l: List[str] = None
    for line in sys.stdin:
        line = line.strip()
        if line:  # If line is not blank
            buf += line + " "  # 'key: value ' -> final space
        else:
            # print(buf)
            l = re.split(r' |:', buf.strip())
            l = [ele for index, ele in enumerate(l) if index%2 == 0]
            # print(l)
            s: Set[str] = set(l) ^ set(required_fields) 
            # print(s)
            if not s or (len(s) == 1 and s.pop() == 'cid'):
                count += 1
            buf = ''
    print(count)

if __name__ == "__main__":
    main()

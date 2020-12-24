"""
Day 5, part 2 - Binary Boarding

https://adventofcode.com/2020/day/5

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
import re

def main():
    ids: List[int] = list()
    for line in sys.stdin:
        line = line.strip()
        if not line:  # Blank line
            continue
        r_str: str = line[:7]  # Row string identifier
        c_str: str = line[7:]  # Col string identifier
        r_str_bin:str = ''.join(list(map(lambda x: '0' if x == 'F' else '1', r_str)))
        r_id: int = int(r_str_bin, 2)
        c_str_bin:str = ''.join(list(map(lambda x: '0' if x == 'L' else '1', c_str)))
        c_id: int = int(c_str_bin, 2)
        current_id: int = r_id * 8 + c_id
        ids.append(current_id)
    ids.sort()
    # print(ids)
    missing_id: int = -1
    prev_ele: int = ids[0]
    for ele in ids[1:]:
        if ele != prev_ele+1:
            missing_id = ele-1
            break
        prev_ele = ele
    print(missing_id)

if __name__ == "__main__":
    main()
